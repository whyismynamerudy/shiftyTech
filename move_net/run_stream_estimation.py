import numpy as np
import tensorflow as tf

from move_net.estimation import movenet, input_size
from move_net.helper import draw_prediction_on_image, to_gif
from move_net.stream_estimation_helpers import init_crop_region, run_inference, determine_crop_region

# Load the input image.
image_path = '/move_net/dance.gif'
image = tf.io.read_file(image_path)
image = tf.image.decode_gif(image)

# Load the input image.
num_frames, image_height, image_width, _ = image.shape
crop_region = init_crop_region(image_height, image_width)

output_images = []
for frame_idx in range(num_frames):
    keypoints_with_scores = run_inference(
        movenet, image[frame_idx, :, :, :], crop_region,
        crop_size=[input_size, input_size])
    output_images.append(draw_prediction_on_image(
        image[frame_idx, :, :, :].numpy().astype(np.int32),
        keypoints_with_scores, crop_region=None,
        close_figure=True, output_image_height=300))
    crop_region = determine_crop_region(
        keypoints_with_scores, image_height, image_width)

# Prepare gif visualization.
output = np.stack(output_images, axis=0)
to_gif(output, duration=100)
