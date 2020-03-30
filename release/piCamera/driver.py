import time

import cv2
import myro
from img import mask


def orient(image_thread, window_name, calibration, comPort):
    """Determine the front of the robot.

    Spins the robot, then moves forward and calculates the
    centroid delta. This delta is used to determine the orientation
    of the robot. It is spun until it is 'facing' up.

    Args:
        image_thread: A thread that constantly returns new images from the camera.
        window_name: The name of the window the user sees to update.
        calibration: K-means calibration for frame masking.
        comPort: Port of Scribbler 2 to connect to. # TODO: Global init is necessary.

    Returns:
        An integer representing an exit status, and the coordinates of the front.

        -1, None: User indicated quit (Q or ESC in CV2 Window).
        0, (X, Y): Found front coordinates successfully.

    Raises:
        None
    """
    # TODO: Add auto kill if calibration fails.
    debug = False
    done = False
    myro.init(comPort)

    while not done:
        # Grab a frame pre-movement.
        frame = image_thread.read()
        frame, (cX, cY) = mask(frame, calibration)
        cv2.imshow(window_name, frame)

        # Move some direction.
        myro.forward(1, 0.5)
        time.sleep(0.1)

        # Grab a frame post-movement.
        frame = image_thread.read()
        frame, (cX2, cY2) = mask(frame, calibration)

        # Update the user.
        cv2.imshow(window_name, frame)
        key_press = cv2.waitKey(1)

        # Kill on Q or ESC.
        if key_press == 27 or key_press == ord("q"):
            myro.stop()
            return -1

        # Calculate the delta
        dX = cX2 - cX
        dY = cY2 - cY

        # Moving straight vertically indicated calibration was successful.
        if abs(dX) < 5 and dY < 5:
            if debug:
                print("Calibrated", dX, dY)

            frame, (cX, cY) = mask(frame, calibration)
            done = True
            return 0, (cX, cY - 50)
        # Otherwise, rotate and repeat the whole cycle.
        else:
            myro.backward(1, 0.5)
            time.sleep(0.1)
            myro.turnBy(10, "deg")

            if debug:
                print(dX, dY)
