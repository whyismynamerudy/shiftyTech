import tensorflow as tf

from move_net.estimation import input_size, movenet


def get_vector_from_keypoints(keypoints_with_scores):
    # Remove any singleton dimensions
    keypoints_with_scores = tf.squeeze(keypoints_with_scores, axis=1)

    # Slice out the scores to get only the x, y coordinates
    keypoints = keypoints_with_scores[0, :, :2]  # [17, 2]

    # Flatten the keypoints tensor
    flattened_vector = tf.reshape(keypoints, [-1])  # [34]

    normalized_vector = tf.nn.l2_normalize(flattened_vector, axis=0)

    return normalized_vector.numpy()


def get_vector_from_image(image_path_internal):
    vector_image = tf.io.read_file(image_path_internal)
    vector_image = tf.image.decode_jpeg(vector_image)
    input_image = tf.expand_dims(vector_image, axis=0)
    input_image = tf.image.resize_with_pad(input_image, input_size, input_size)

    return get_vector_from_keypoints(movenet(input_image))
