import time

import cv2

from tracker import calibrate
from tracker import ImageThread
from tracker import mask
from tracker import orient

# For now, only CV2 color-based detection is supported and working properly.

if __name__ == "__main__":
    URL = "http://Zeta.lan:8000/stream.mjpg"
    COM_PORT = "COM5"

    image_thread = ImageThread(URL).start()
    time.sleep(0.1)

    calibration = None
    front_coords = None

    while True:
        frame = image_thread.read()
        if calibration is not None:
            frame, (cX, cY) = mask(frame, calibration)
        if front_coords is not None:
            cv2.circle(frame, front_coords, 7, (0, 255, 0), -1)
        # If not calibrated, just show the image.
        cv2.imshow("frame", frame)

        # Handle all keypress events
        key_press = cv2.waitKey(1)

        # Quit on escape or q
        if key_press == 27 or key_press == ord("q"):
            image_thread.stop()
            exit(0)
        # Calibrate on n, if calibration exists, reset.
        elif key_press == ord("n"):
            if calibration is not None:
                calibration = None
                continue
            calibration = calibrate(frame)
        # Orient
        elif key_press == ord("o"):
            if calibrate is None:
                print("Calibrate first!")
            else:
                ret, front_coords = orient(image_thread, "frame", calibration, COM_PORT)
                if ret != 0:
                    image_thread.stop()
                    exit(0)
