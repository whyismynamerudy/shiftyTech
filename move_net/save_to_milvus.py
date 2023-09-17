import configparser
import os

from pymilvus import connections, utility
from pymilvus import Collection

from move_net.image_utils import get_vector_from_image

# Load milvus configs
cfp = configparser.RawConfigParser()
cfp.read('../config_serverless.ini')

# Connect to milvus
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

shifty_collection = Collection(collection_name)


def store_vector_in_milvus(image_name, vector_internal):
    """
    Store the vector in Milvus.
    """
    coll_name = "shifty_collection"
    shifty = Collection(coll_name)
    entities = [
        {"vector": vector_internal, "image_name": image_name}
    ]
    shifty.insert(entities)


mocks_folder = '../mocks'
all_images = [f for f in os.listdir(mocks_folder) if f.endswith('.jpg') or f.endswith('jpeg')]

for image in all_images:
    print("on image: ", image)
    image_path = os.path.join(mocks_folder, image)
    vector = get_vector_from_image(image_path)
    store_vector_in_milvus(image, vector)

print("Uploaded all vectors to Milvus!")

