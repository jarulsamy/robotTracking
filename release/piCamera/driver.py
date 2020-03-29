import myro
from img import mask
import numpy as np
import threading
from collections import deque


class DriverThread():
    def __init__(self, image_thread, calibration, comPort="COM5", buffer=20):
        # threading.Thread.__init__(self)
        self.image_thread = image_thread
        self.calibration = calibration
        self.buffer = buffer
        self.pts = deque(maxlen=self.buffer)
        self.stopped = False

        myro.init(comPort)

    def start(self):
        threading.Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            frame = self.image_thread.read()
            self.frame, (cX, cY) = mask(frame, self.calibration)
            self.center = (cX, cY)
            self.orient()

    def get_frame(self):
        return self.frame

    def reset(self):
        self.pts = deque(maxlen=self.buffer)

    def quit(self):
        myro.stop()

    def orient(self):
        (dX, dY) = (0, 0)
        direction = ""

        self.pts.append(self.center)

        for i in np.arange(1, len(self.pts)):
            if self.pts[i - 1] is None or self.pts[i] is None:
                continue
            # check to see if enough points have been accumulated in
            # the buffer
            if len(self.pts) >= 10 and i == 1 and self.pts[-10] is not None:
                # compute the difference between the x and y
                # coordinates and re-initialize the direction
                # text variables
                dX = self.pts[-10][0] - self.pts[i][0]
                dY = self.pts[-10][1] - self.pts[i][1]
                (dirX, dirY) = ("", "")
                # ensure there is significant movement in the
                # x-direction
                if np.abs(dX) > 20:
                    dirX = "West" if np.sign(dX) == 1 else "East"
                # ensure there is significant movement in the
                # y-direction
                if np.abs(dY) > 20:
                    dirY = "South" if np.sign(dY) == 1 else "North"
                # handle when both dqirections are non-empty
                if dirX != "" and dirY != "":
                    direction = "{}-{}".format(dirY, dirX)
                # otherwise, only one direction is non-empty
                else:
                    direction = dirX if dirX != "" else dirY

        print(direction, dX, dY)
