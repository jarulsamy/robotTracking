import sys
sys.path.insert(0, 'C:\Python27\myro')
from myro import *
import cv2
import numpy as np
import urllib


#Downloads picture from Kaicong webui 
#urllib.urlretrieve("http://192.168.0.100:81/snapshot.cgi?loginuse=admin&loginpas=123456","img.jpg")
#global origPic
origPic = cv2.imread("img.jpg")
height, width, channels = origPic.shape
chassisPic = origPic

# Set global parameters
RED = 0
GREEN = 1
BLUE = 2

# Load the image
img_color = cv2.imread("img.jpg", flags=cv2.IMREAD_COLOR)

# Filter the image by desired color
img_color_filtered = np.asarray([y[GREEN] for x in img_color for y in x]).reshape((img_color.shape[:2]))

cv2.imshow("orig", img_color_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()




red = origPic[:, :, 2]
cv2.imshow("img", red)
cv2.imshow("orig", origPic)
cv2.waitKey(0)
cv2.destroyAllWindows()
