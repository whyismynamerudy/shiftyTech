# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Import TF and TF Hub libraries.
import configparser
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from sklearn import neighbors
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymilvus import connections, utility
from pymilvus import Collection
import os

K = 1

uri = "mongodb+srv://shiftytechtech:shiftytechtech@shifty-cluster.cvt1acl.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

# Access the specified database and collection
db = client['shifty-db']
collection = db['shifty-collection']

cfp = configparser.RawConfigParser()
cfp.read('config_serverless.ini')
milvus_uri = cfp.get('example', 'uri')
token = cfp.get('example', 'token')

connections.connect("default",
                    uri=milvus_uri,
                    token=token)
print(f"Connecting to DB: {milvus_uri}")

# Check if the collection exists
collection_name = "shifty_collection"
check_collection = utility.has_collection(collection_name)
print("Successfully connected to collection!")


# Function to store vectors in the database
def store_vector(vector, label):
    # You can customize how you want to store the vector.
    # Here's a basic example:
    data = {
        'label': label,
        'vector': vector.tolist()  # Convert numpy array to a list for storage
    }
    collection.insert_one(data)


# Function to retrieve all vectors from the database
def retrieve_vectors():
    vectors = []
    internal_labels = []
    for doc in collection.find():
        vectors.append(np.array(doc['vector']))
        internal_labels.append(doc['label'])
    return np.array(vectors), np.array(internal_labels)


def search_nearest_vector(query_vector, k=1):
    milv_coll = Collection("shifty_collection")
    milv_coll.load()
    search_params = {
        "metric_type": "L2",
        "offset": 0,
        "ignore_growing": False,
        "params": {}
    }
    results = milv_coll.search(
        data=[query_vector],
        anns_field="vector",
        param=search_params,
        limit=1,
        output_fields=["image_name"]
    )
    return results[0][0]


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Download the model from TF Hub.
# Load the model from the local directory.
model = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
movenet = model.signatures['serving_default']

cosine_loss = tf.keras.losses.CosineSimilarity(axis=0)
neigh = neighbors.KNeighborsClassifier(n_neighbors=1)


def get_vector_old(path, to_rotate=True):
    image = tf.io.read_file(path)
    image = tf.compat.v1.image.decode_jpeg(image)
    if to_rotate:
        image = tf.image.rot90(image, k=3)  # Rotate the image 90 degrees clockwise
    image = tf.expand_dims(image, axis=0)
    # Resize and pad the image to keep the aspect ratio and fit the expected size.
    image = tf.cast(tf.image.resize_with_pad(image, 192, 192), dtype=tf.int32)

    # Run model inference.
    outputs = movenet(image)

    # Output is a [1, 1, 17, 3] tensor.
    keypoints = outputs['output_0']
    new_img = keypoints[:, :, :, :2].numpy().squeeze()
    y_values, x_values = tf.unstack(new_img, axis=1)

    # Reshape
    full_vector = tf.reshape(tf.stack([x_values, y_values], axis=1), [-1, 1])
    # Concatenate the two segments
    final_vector = tf.concat(full_vector, axis=0)

    return final_vector


def read_and_preprocess_image(path, to_rotate=True):
    """Reads an image from the given path and applies the necessary preprocessing."""
    image = tf.io.read_file(path)
    image = tf.compat.v1.image.decode_jpeg(image)
    if to_rotate:
        image = tf.image.rot90(image, k=3)  # Rotate the image 90 degrees clockwise
    # Resize and pad the image to keep the aspect ratio and fit the expected size.
    image = tf.cast(tf.image.resize_with_pad(image, 192, 192), dtype=tf.int32)
    return tf.expand_dims(image, axis=0)


def extract_keypoints(image):
    """Extracts keypoints from the image using the MoveNet model."""
    outputs = movenet(image)
    return outputs['output_0']


def process_keypoints(keypoints):
    """Processes the extracted keypoints to form the final vector."""
    new_img = keypoints[:, :, :, :2].numpy().squeeze()
    y_values, x_values = tf.unstack(new_img, axis=1)
    full_vector = tf.reshape(tf.stack([x_values, y_values], axis=1), [-1, 1])
    return full_vector


def normalize_vector(vector):
    """Normalizes the vector to have a mean of zero and a standard deviation of one."""
    mean, variance = tf.nn.moments(vector, axes=0)
    std_dev = tf.sqrt(variance)
    return (vector - mean) / std_dev


def get_vector(path, to_rotate=True):
    image = read_and_preprocess_image(path, to_rotate)
    keypoints = extract_keypoints(image)
    vector = process_keypoints(keypoints)
    normalized_vector = normalize_vector(vector)
    return normalized_vector


def get_all_images_from_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    print("files: ", files)
    # Filter out the images (assuming jpg format for simplicity)
    images = [f for f in files if f.endswith('.jpeg')]
    return images


# Define a function to store vectors in MongoDB
def store_vector_in_mongo(image_name, vector):
    data = {
        'image_name': image_name,
        'vector': vector.numpy().flatten().tolist()  # Convert numpy array to a list for storage
    }
    collection.insert_one(data)


def store_vector_in_milvus(image_name, vector):
    """
    Store the vector in Milvus.
    """
    coll_name = "shifty_collection"
    shifty = Collection(coll_name)
    entities = [
        {"vector": vector, "image_name": image_name}
    ]
    shifty.insert(entities)


def store_mocks():
    # List all images in the "mocks" folder
    mocks_folder = 'mocks'
    all_images = [f for f in os.listdir(mocks_folder) if
                  f.endswith('.jpg') or f.endswith('jpeg')]  # Assuming jpg images

    # For each image, extract its feature vector and store in MongoDB
    for image in all_images:
        print("on image: ", image)
        image_path = os.path.join(mocks_folder, image)
        vector = get_vector(image_path, to_rotate=False)
        store_vector_in_milvus(image, vector)

    print("Uploaded all vectors to Milvus!")


# store_mocks()

############## USEFUL CODE ABOVE #################

'''
Below:
    . given input image, call the respective function and return its predicted output.
'''


def estimate(frame):
    # Convert the numpy frame to a TensorFlow tensor.
    image_tensor = tf.convert_to_tensor(frame)

    # Resize and preprocess the image for MoveNet.
    preprocessed_image = tf.cast(tf.image.resize_with_pad(image_tensor, 192, 192), dtype=tf.int32)
    preprocessed_image = tf.expand_dims(preprocessed_image, axis=0)

    # Extract keypoints from the preprocessed image.
    keypoints = extract_keypoints(preprocessed_image)

    # Process and normalize the keypoints to get the vector.
    vector = process_keypoints(keypoints)
    normalized_vector = normalize_vector(vector)

    # Convert the normalized vector to the appropriate format for Milvus search.
    query_vector = normalized_vector.numpy().flatten().tolist()

    # Search for the most similar vector in Milvus.
    result = search_nearest_vector(query_vector)

    # The result contains the most similar image's name from the Milvus collection.
    # This assumes that the 'image_name' field in the Milvus collection refers to the name of the similar image.
    similar_image_name = result.entity.get('image_name')

    return similar_image_name


# folder_path = './images'
# all_images = get_all_images_from_folder(folder_path)
#
# print("Images we are referencing: ", all_images)
#
# # Assuming `get_vector` and `search_nearest_vector` are already defined in your script
# similarity_results = {}
#
# for image in all_images:
#     image_path = os.path.join(folder_path, image)
#     vector = get_vector(image_path).numpy().flatten()
#
#     # Perform similarity search
#     img = search_nearest_vector(vector)
#
#     # Store the results
#     similarity_results[image] = img.entity.get('image_name')
#
# for image, similar_imgs in similarity_results.items():
#     print(f"Image: {image}")
#     print(f"Most similar images: {similar_imgs}")
#     print("----------")

if __name__ == '__main__':
    print('don\'t run me :(')
    print('but now you did, im storing image vectors in milvus')
    store_mocks()
