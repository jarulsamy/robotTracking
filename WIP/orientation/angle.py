import math
import numpy as np
import cv2

pic1 = cv2.imread("1.jpg")
# pic2 = cv2.imread("2.jpg")

redUpper = np.array([80, 40,  255], dtype=np.uint8) # Upper threshold for chassis ID # HSV VERSION
redLower = np.array([0, 20, 0], dtype=np.uint8) #Lower threshold for chassis ID # HSV VERSION

blueUpper = np.array([255, 180,  10], dtype=np.uint8) # Upper threshold for chassis ID # HSV VERSION
blueLower = np.array([230, 160, 0], dtype=np.uint8) #Lower threshold for chassis ID # HSV VERSION



maskRed = cv2.inRange(pic1, redLower, redUpper)
edgeRed = cv2.Canny(maskRed, 75, 200)
im2, contoursRed, hierarchy = cv2.findContours(edgeRed, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(pic1, contoursRed, -1, (0,255,0), 2)

maskBlue = cv2.inRange(pic1, blueLower, blueUpper)
edgeBlue = cv2.Canny(maskBlue, 75, 200)
im2, contoursBlue, hierarchy = cv2.findContours(edgeBlue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(pic1, contoursBlue, -1, (0,0,255),2)

# for contours in contoursRed:
#     mRed = cv2.moments(contours)
#     xRed = int(mRed['m10']/mRed['m00'])
#     yRed = int(mRed['m01']/mRed['m00'])
#     cv2.circle(pic1, (xRed, yRed), 10, (0, 255, 0), -20)
#     centroidRed = (xRed, yRed)

cv2.imshow("ofoo", pic1)
cv2.waitKey(0)
cv2.destroyAllWindows()
