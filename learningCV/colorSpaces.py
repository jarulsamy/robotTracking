import sys
#sys.path.insert(0, 'E:\Python27\myro')
#from myro import *
import cv2
import numpy as np
import urllib
import argparse
### Variables for click_and_crop ###
mousePoint = []
cropping = False
### Variables for click_and_crop ###

	# Mouse point Drawing

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global mousePoint, cropping
	if event == cv2.EVENT_LBUTTONDOWN:
		print('foo')
		mousePoint = [(x, y)]
		cropping = True
		mousePoint.append((x, y))
		cropping = False
		# draw a rectangle around the region of interest
		cv2.rectangle(finalImage, mousePoint[0], mousePoint[1], (0, 255, 0), 2)
		cv2.imshow("Final", finalImage)

cv2.namedWindow("Final")
cv2.setMouseCallback("Final", click_and_crop)

### Mouse Point Drawing End ###
### Inital Variable Decleration ###
kernel = np.ones((5,5), np.uint8)
origPic = cv2.imread("img.jpg")
maxContour = 0
### Inital Variable Decleration ###

### GOOD COLOR SPACES ###
# HSV
# BGR2RGB NOT GREAT BUT REALLY COOL
# LUV
# HLS
#
redLower = (0, 0, 200)
redUpper = (30, 100, 255)
altColorSpaceImg = cv2.cvtColor(origPic, cv2.COLOR_BGR2HLS)
blurredImg = cv2.GaussianBlur(altColorSpaceImg, (11, 11), 10) #Blurs image to deal with noise
blurredImg = cv2.bilateralFilter(blurredImg, 25, 75, 75) #Uses bilaterial filtering to deal with more noise
mask = cv2.inRange(blurredImg, redLower, redUpper)
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)
### Mask Stuff END ###

### Contour Stuff ###
im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
cnt = contours[0]
cv2.drawContours(mask, contours, -1, (0,0,255), 2) #Draw countours on ALT Image
# Finds Largest blob

for contour in contours:
	contourSize = cv2.contourArea(cnt)
	if contourSize > maxContour:
		maxContour = contourSize
		maxContourData = contour

areaMask = np.zeros_like(mask)

cv2.fillPoly(areaMask,[maxContourData],1) # Draws new areaMask onto new image

R,G,B = cv2.split(blurredImg) #Splits image in to RGB Values
# Creates solid black image + mask
finalImage = np.zeros_like(blurredImg)
finalImage[:,:,0] = np.multiply(R,areaMask)
finalImage[:,:,1] = np.multiply(G,areaMask)
finalImage[:,:,2] = np.multiply(B,areaMask)
# Contour Stuff End ###

### Show Images ###
cv2.imshow('Mask',mask)
cv2.imshow('Alternative Color Space Image', altColorSpaceImg)
cv2.imshow('Final',finalImage)
cv2.waitKey(0)
### Show Images END ###
