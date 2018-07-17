# Standard imports
import cv2
import numpy as np

URL = "http://10.0.0.101:8000/stream.mjpg"
cap = cv2.VideoCapture(URL)

while True:
    ret, frame = cap.read()
    
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray", im)
    # im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)

    detector = cv2.SimpleBlobDetector_create()

    keypoints = detector.detect(im)

    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array(
        []), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    if cv2.waitKey(1) == 27:
        exit(0)