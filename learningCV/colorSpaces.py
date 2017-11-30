import sys
sys.path.insert(0, 'C:\Python27\myro')
from myro import *
import cv2
import numpy as np
import urllib

origPic = cv2.imread("img.jpg")

### GOOD COLOR SPACES ###
# HSV
# BGR2RGB NOT GREAT BUT REALLY COOL
# LUV
# HLS
#
redLower = (0, 0, 200)
redUpper = (30, 100, 255)
chassisPic = cv2.cvtColor(origPic, cv2.COLOR_BGR2HLS)
mask = cv2.inRange(chassisPic, redLower, redUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

cv2.imshow("New", mask)
cv2.imshow("Old", chassisPic)
cv2.waitKey(0)
cv2.destroyAllWindows()