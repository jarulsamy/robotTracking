import myro
from img import mask
import cv2
import time


def orient(image_thread, window_name, calibration, comPort):
    debug = False
    done = False
    myro.init(comPort)
    while not done:
        frame = image_thread.read()
        frame, (cX, cY) = mask(frame, calibration)
        cv2.imshow(window_name, frame)

        myro.forward(1, 0.5)
        time.sleep(0.1)

        frame = image_thread.read()
        frame, (cX2, cY2) = mask(frame, calibration)

        cv2.imshow(window_name, frame)
        key_press = cv2.waitKey(1)

        if key_press == 27 or key_press == ord("q"):
            myro.stop()
            return -1

        dX = cX2 - cX
        dY = cY2 - cY

        if abs(dX) < 5 and dY < 5:
            if debug:
                print("Calibrated", dX, dY)

            frame, (cX, cY) = mask(frame, calibration)
            done = True
            return 0, (cX, cY - 50)
        else:
            myro.backward(1, 0.5)
            time.sleep(0.1)
            myro.turnBy(10, "deg")

            if debug:
                print(dX, dY)
