import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
origPic = cv2.imread("img.jpg")
maxContour = 0
greenUpper = np.array([200, 200, 255], dtype=np.uint8) #Thresholds for board ID
greenLower = np.array([0, 0, 150], dtype=np.uint8) #Thresholds for board ID
