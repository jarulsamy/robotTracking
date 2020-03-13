import cv2
import threading
import numpy as np


class ImageThread(threading.Thread):
    def __init__(self, threadID, URL):
        threading.Thread.__init__(self)
        self.id = threadID
        self.URL = URL
        self.cap = cv2.VideoCapture(URL)

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame


def calibrate(frame):
    # cv2.imshow("Calibration", frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    r = cv2.selectROI("ROI", frame)
    cv2.destroyWindow("ROI")
    imCrop = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    # Use k-means clustering to create a palette
    # with the most representative colors in the region
    pixels = np.float32(imCrop.reshape(-1, 3))
    n_colors = 5

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(
        pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)

    dominant = palette[np.argmax(counts)]
    return dominant


def mask(img, color, thresh_delta=50):
    kernel = np.ones((5, 5), np.uint8)

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = color - thresh_delta
    upper = color + thresh_delta
    masked_img = cv2.inRange(hsv_img, lower, upper)
    masked_img = cv2.dilate(masked_img, kernel, iterations=5)
    edges = cv2.Canny(masked_img, 75, 200)

    # find contours in the thresholded image
    contours, hierarchy = cv2.findContours(
        edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours):
        c = [cv2.convexHull(cnt) for cnt in contours]
        c = max(c, key=cv2.contourArea)
        cv2.drawContours(img, c, -1, (0, 255, 0), 2)

        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img, (cX, cY), 7, (0, 255, 0), -1)

    return img, (cX, cY)
