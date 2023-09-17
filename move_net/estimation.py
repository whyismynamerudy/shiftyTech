import tensorflow as tf
import tensorflow_hub as hub
import requests

model_name = "movenet_thunder"


def download_model(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)


if "tflite" in model_name:
    if "movenet_lightning_f16" in model_name:
        download_model(
            "https://tfhub.dev/google/lite-model/movenet/singlepose/lightning/tflite/float16/4?lite-format=tflite",
            "model.tflite")
        input_size = 192
    elif "movenet_thunder_f16" in model_name:
        download_model(
            "https://tfhub.dev/google/lite-model/movenet/singlepose/thunder/tflite/float16/4?lite-format=tflite",
            "model.tflite")
        input_size = 256
    elif "movenet_lightning_int8" in model_name:
        download_model(
            "https://tfhub.dev/google/lite-model/movenet/singlepose/lightning/tflite/int8/4?lite-format=tflite",
            "model.tflite")
        input_size = 192
    elif "movenet_thunder_int8" in model_name:
        download_model(
            "https://tfhub.dev/google/lite-model/movenet/singlepose/thunder/tflite/int8/4?lite-format=tflite",
            "model.tflite")
        input_size = 256
    else:
        raise ValueError("Unsupported model name: %s" % model_name)

    interpreter = tf.lite.Interpreter(model_path="model.tflite")
    interpreter.allocate_tensors()


    def movenet(input_image):
        input_image = tf.cast(input_image, dtype=tf.uint8)
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        interpreter.set_tensor(input_details[0]['index'], input_image.numpy())
        interpreter.invoke()
        keypoints_with_scores = interpreter.get_tensor(output_details[0]['index'])
        return keypoints_with_scores

else:
    if "movenet_lightning" in model_name:
        module = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")
        input_size = 192
    elif "movenet_thunder" in model_name:
        module = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
        input_size = 256
    else:
        raise ValueError("Unsupported model name: %s" % model_name)


    def movenet(input_image):
        model = module.signatures['serving_default']
        input_image = tf.cast(input_image, dtype=tf.int32)
        outputs = model(input_image)
        keypoints_with_scores = outputs['output_0'].numpy()
        return keypoints_with_scores


