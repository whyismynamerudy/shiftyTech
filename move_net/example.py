import os
from pathlib import Path

import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt

from move_net.estimation import movenet, input_size
from move_net.helper import draw_prediction_on_image

# Directory paths
mocks_directory = '../mocks/'
test_directory = '../test/'

# Create test directory if it doesn't exist
Path(test_directory).mkdir(parents=True, exist_ok=True)

# Iterate over all images in the mocks directory
for filename in os.listdir(mocks_directory):
    if filename.endswith(".jpg"):  # You can add more formats if needed
        image_path = os.path.join(mocks_directory, filename)

        # Load the image
        image = tf.io.read_file(image_path)
        image = tf.image.decode_jpeg(image)

        # Resize and pad the image
        input_image = tf.expand_dims(image, axis=0)
        input_image = tf.image.resize_with_pad(input_image, input_size, input_size)

        # Run model inference
        keypoints_with_scores = movenet(input_image)

        # Visualize the predictions with image
        display_image = tf.expand_dims(image, axis=0)
        display_image = tf.cast(tf.image.resize_with_pad(display_image, 1280, 1280), dtype=tf.int32)
        output_overlay = draw_prediction_on_image(np.squeeze(display_image.numpy(), axis=0), keypoints_with_scores)

        # Save the overlayed image to the test directory
        output_path = os.path.join(test_directory, filename)
        plt.imsave(output_path, output_overlay)
