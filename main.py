import webbrowser
import pyautogui
import time
import cv2


def main():
    url = "https://replit.com/join/fmrnbraiil-rudrakshmonga1" # replace later, figure out how to input, wtv
    webbrowser.open(url)

    time.sleep(3)

    pyautogui.click(x=558, y=318)
    pyautogui.write('Hello world!', interval=0.1)

    vid = cv2.VideoCapture(0)
    while(True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if name == 'main':
    main()