import sys
#sys.path.insert(0, 'E:\Python27\myro')
#from myro import *
import cv2
import numpy as np
import urllib
### Variables for click_and_crop ###
mousePoint = []
cropping = False
### Variables for click_and_crop ###

	# Mouse point Drawing

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global mousePoint, cropping
	if event == cv2.EVENT_LBUTTONDOWN:
		mousePoint = [(x, y)]
		cropping = True
		mousePoint.append((x, y))
		cropping = False
		cv2.rectangle(origPic, mousePoint[0], mousePoint[1], (0, 255, 0), 10)
		cv2.imshow("Original", origPic)
	if event == cv2.EVENT_RBUTTONDOWN:
		boardPoint = [(x, y)]
		cropping = True
		boardPoint.append((x, y))
		cropping = False
		cv2.rectangle(origPic, boardPoint[0], boardPoint[1], (0, 0, 255), 10)
		cv2.imshow("Original", origPic)

cv2.namedWindow("Original")
cv2.setMouseCallback("Original", click_and_crop)

### Mouse Point Drawing End ###
kernel = np.ones((5,5), np.uint8)
origPic = cv2.imread("img.jpg")
# origPic = cv2.imread("2.jpg")
maxContour = 0

### GOOD COLOR SPACES ###

# HSV
# BGR2RGB NOT GREAT BUT REALLY COOL
# LUV
# HLS
# B G R
# YCrCb Seems to be a little fuzzy for some reason
redUpper = np.array([200, 200, 255], dtype=np.uint8) #Thresholds for Chassis ID
redLower = np.array([0, 0, 150], dtype=np.uint8) #Thresholds for Chassis ID

greenUpper = np.array([255, 255, 255], dtype=np.uint8) #Thresholds for Board ID
greenLower = np.array([0, 0, 0], dtype=np.uint8) #Thresholds for Board ID

### Chassis Masks ###

altChassis = cv2.cvtColor(origPic, cv2.COLOR_BGR2YUV)
blurredImgChassis = cv2.GaussianBlur(altChassis, (11, 11), 10) #Blurs image to deal with noise
blurredImgChassis = cv2.bilateralFilter(blurredImgChassis, 25, 75, 75) #Uses bilaterial filtering to deal with more noise
maskChassis = cv2.inRange(blurredImgChassis, redLower, redUpper) # Thesholds the image to grab in range pixels
maskChassis = cv2.erode(maskChassis, kernel, iterations=2) # Erodes to remove small imperfections
maskChassis = cv2.dilate(maskChassis, kernel, iterations=2) # Dialates to remove small imperfections

### Board Masks ###

# altBoard = cv2.cvtColor(origPic, cv2.COLOR_BGR2LAB)
altBoard = cv2.cvtColor(origPic, cv2.COLOR_BGR2YCR_CB)
blurredImgBoard = cv2.GaussianBlur(altBoard, (11, 11), 10) #Blurs image to deal with noise
blurredImgBoard = cv2.bilateralFilter(blurredImgBoard, 25, 75, 75) #Uses bilaterial filtering to deal with more noise
maskBoard = cv2.inRange(blurredImgBoard, greenLower, greenUpper) # Erodes to remove small imperfections
maskBoard = cv2.erode(maskBoard, kernel, iterations=2) # Erodes to remove small imperfections
maskBoard = cv2.dilate(maskBoard, kernel, iterations=2) # Dialates to remove small imperfections

### Chassis Contours ###

contour_list_chassis = []
im2Chassis, contoursChassis, hierarchyChassis = cv2.findContours(maskChassis, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
try:
	cnt = contoursChassis[0]
except IndexError:
	print('indexERror')
for contour in contoursChassis:
	approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
	area = cv2.contourArea(contour)
	if ((len(approx) > 12) & (area > 1000)): # This seems to work regardless of what area is, investigate
		contour_list_chassis.append(contour)
cv2.drawContours(altChassis, contour_list_chassis, -1, (0,0,255), 2)

### Board Contours ###

contour_list_board = []
im2Board, contoursBoard, hierarchyBoard = cv2.findContours(maskBoard, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
cnt = contoursBoard[0]

for contour in contoursBoard:
	approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
	area = cv2.contourArea(contour)
	if ((len(approx) > 12) & (area > 1000)): # This seems to work regardless of what area is, investigate
		contour_list_board.append(contour)
cv2.drawContours(altBoard, contour_list_board, -1, (0,0,255), 2)


### EXPERIMENTAL ###

img_rgb = cv2.imread('img.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg ',0)

w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(altChassis, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

### EXPERIMENTAL

# Chassis
cv2.imshow('Alt Chassis', altChassis)
# cv2.imshow('Mask Chassis',maskChassis)
# Board
cv2.imshow('Alt Board', altBoard)
cv2.imshow('Mask Board', maskBoard)
# Original
cv2.imshow('Original', origPic)
# Exit K
cv2.waitKey(0)
