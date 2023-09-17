import webbrowser
import pyautogui
import time
import cv2
# Assuming the helper and estimation modules are in the "move_net" directory
from move_net.estimation import movenet, input_size
from move_net.helper import draw_prediction_on_image
import tensorflow as tf


def main():
    url = "https://replit.com/join/fmrnbraiil-rudrakshmonga1"
    webbrowser.open(url)

    time.sleep(5)

    pyautogui.click(x=558, y=318)
    pyautogui.write("print('Hello Worlddd!')", interval=0.01)

    vid = cv2.VideoCapture(1)
    frame_interval = 3  # Set the frame capture interval in seconds
    start_time = time.time()

    while True:
        current_time = time.time()
        time_left = frame_interval - (current_time - start_time)

        ret, frame = vid.read()

        # Create an image with the same dimensions as the frame for the text overlay
        overlay = frame.copy()

        # Add text indicating the time left until the next frame capture
        text = f"Next frame in {int(time_left) + 1}"
        cv2.putText(overlay, text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 2)

        # Blend the overlay text onto the frame
        alpha = 0.6  # Adjust the transparency of the text
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        # Run MoveNet inference on the current frame
        input_image = tf.image.resize(frame, [input_size, input_size])
        input_image = tf.expand_dims(input_image, axis=0)

        keypoints_with_scores = movenet(input_image)

        # Draw the keypoints onto the frame
        frame = draw_prediction_on_image(frame, keypoints_with_scores)

        cv2.imshow('frame', frame)

        if time_left <= 0:
            # Capture a frame and reset the start time for the next frame capture
            ret, frame = vid.read()
            start_time = time.time()

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
