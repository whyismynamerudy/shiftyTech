import webbrowser
import pyautogui
import time
import cv2
from model import estimate


def main():
    url = "https://replit.com/join/fmrnbraiil-rudrakshmonga1" # replace later, figure out how to input, wtv
    webbrowser.open(url)

    time.sleep(5)

    pyautogui.click(x=558, y=318)
    pyautogui.write("print('Hello Worlddd!')", interval=0.01)

    vid = cv2.VideoCapture(0)
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

        cv2.imshow('frame', frame)

        if time_left <= 0:
            # Capture a frame and reset the start time for the next frame capture
            ret, frame = vid.read()
            start_time = time.time()
            # estimate(frame)

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