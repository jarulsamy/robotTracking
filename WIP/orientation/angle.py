import math
import numpy as np
import cv2

pic1 = cv2.imread("2.jpg")
# pic2 = cv2.imread("2.jpg")

redUpper = np.array([80, 40,  255], dtype=np.uint8) # Upper threshold for chassis ID # HSV VERSION
redLower = np.array([0, 20, 0], dtype=np.uint8) #Lower threshold for chassis ID # HSV VERSION

blueUpper = np.array([255, 180,  10], dtype=np.uint8) # Upper threshold for chassis ID # HSV VERSION
blueLower = np.array([230, 160, 0], dtype=np.uint8) #Lower threshold for chassis ID # HSV VERSION


# for contours in contoursRed:
#     mRed = cv2.moments(contours)
#     xRed = int(mRed['m10']/mRed['m00'])
#     yRed = int(mRed['m01']/mRed['m00'])
#     cv2.circle(pic1, (xRed, yRed), 10, (0, 255, 0), -20)
#     centroidRed = (xRed, yRed)

cv2.imshow("ofoo", pic1)
cv2.waitKey(0)
cv2.destroyAllWindows()
