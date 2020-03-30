from img import ImageThread
from img import mask
from img import calibrate
from driver import orient
import time

import cv2
# import numpy as np


if __name__ == "__main__":
    URL = "http://Zeta.lan:8000/stream.mjpg"

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
                ret, front_coords = orient(
                    image_thread, "frame", calibration, "COM5")
                if ret != 0:
                    image_thread.stop()
                    exit(0)
