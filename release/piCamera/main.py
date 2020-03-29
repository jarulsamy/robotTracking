from img import ImageThread
from img import mask
from img import calibrate
from driver import DriverThread
import time

import cv2
# import numpy as np


if __name__ == "__main__":
    URL = "http://Zeta.lan:8000/stream.mjpg"

    image_thread = ImageThread(URL).start()
    time.sleep(0.1)

    driver_thread = None
    calibration = None
    orient = False

    while True:
        frame = image_thread.read()
        if calibration is not None and driver_thread is None:
            frame, (cX, cY) = mask(frame, calibration)
        elif calibration is not None and driver_thread is not None:
            frame = driver_thread.get_frame()

        cv2.imshow("frame", frame)

        # Handle all keypress events
        key_press = cv2.waitKey(1)

        # Quit on escape or q
        if key_press == 27 or key_press == ord("q"):
            image_thread.stop()
            driver_thread.quit()
            exit(0)

        # Calibrate on n, if calibration exists, reset.
        elif key_press == ord("n"):
            if calibration is not None:
                calibration = None
                continue
            calibration = calibrate(frame)

        elif key_press == ord("o"):
            if calibrate is None:
                print("Calibrate first!")
            else:
                driver_thread = DriverThread(
                    image_thread, calibration).start()
        # elif key_press == ord("r"):
        #     driver_thread.reset()
