### Usage: python findRobot.py IP_ADDRESS:PORT COMX
import cv2
import urllib
import numpy as np
import sys
import math
import time
import threading
from classFinal import *


def show_video(jpg):
    redUpper = np.array([200, 255, 200], dtype=np.uint8) # Upper threshold for chassis ID # HSV VERSION
    redLower = np.array([0, 150, 0], dtype=np.uint8) #Lower threshold for chassis ID # HSV VERSION

    greenUpper = np.array([255, 200, 20], dtype=np.uint8) # Upper threshold for board ID
    greenLower = np.array([0, 20, 0], dtype=np.uint8) # Lower threshold for board ID

    kernel = np.ones((5,5), np.uint8)

    # YUV and LUV Work really well here, currenty sets everything robot to white
    readColors = jpg

    global origPic, chassisImg, boardImg
    origPic = readColors # Keeps an original unedited
    chassisImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2HSV) #Converts to LUV for chassis detection
    # boardImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2RGB) #Converts to LUV for chassis detection # This weird double line thing
    # boardImg = cv2.cvtColor(boardImg, cv2.COLOR_RGB2BGR) #Converts to LUV for chassis detection # is to fix a bug
    boardImg = readColors.copy()

    blurredImgChassis = cv2.GaussianBlur(chassisImg, (11, 11), 10) #Blurs image to deal with noise
    maskChassis = cv2.inRange(blurredImgChassis, redLower, redUpper) # Creates blob image based on threshold; redLower and redUpper
    maskChassis = cv2.erode(maskChassis, kernel, iterations=2) # Erodes to get rid of random specks
    maskChassis = cv2.dilate(maskChassis, kernel, iterations=2) # Dialates to get rid of random specks

    blurredImgBoard = cv2.GaussianBlur(boardImg, (11, 11), 10) #Blurs image to deal with noise
    maskBoard = cv2.inRange(blurredImgBoard, greenLower, greenUpper) # Creates blob image based on threshold; greenLower and greenUpper
    maskBoard = cv2.erode(maskBoard, kernel, iterations=2) # Erodes to get rid of random specks
    maskBoard = cv2.dilate(maskBoard, kernel, iterations=2) # Dialates to get rid of random specks

    edgeChassis = cv2.Canny(maskChassis, 75, 200) # Runs cv2.canny to give us better contours
    edgeBoard = cv2.Canny(maskBoard, 75, 200) # Runs cv2.canny to give us better contours

    im2Chassis, contoursChassis, hierarchyChassis = cv2.findContours(edgeChassis, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked chassisimage
    im2Board, contoursBoard, hierarchyBoard = cv2.findContours(edgeBoard, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked borad image

    cv2.drawContours(chassisImg, contoursChassis, -1, (0,0,255), 2) #Draw countours on alternate color space chassis image
    cv2.drawContours(boardImg, contoursBoard, -1, (0,0,255), 2) #Draw countours on alternate color space board image


    checkShape(contoursChassis, contoursBoard)

# Elegant solution to combine color and shape detection for chassis. Looks for most circular contour
def checkShape(contoursChassis, contoursBoard):
    contour_list_chassis = [] # List of all the contours for chassis. Cleared every frame to prevent memory issues
    contour_list_board = [] # List of all the contours for board. Cleared every frame to prevent memory issues

    for contourChassis in contoursChassis:
        approx = cv2.approxPolyDP(contourChassis, 0.01*cv2.arcLength(contourChassis, True), True)
        area = cv2.contourArea(contourChassis)
        if ((len(approx) > 8) & (area > 1000)):
            contour_list_chassis.append(contourChassis)

    for contourBoard in contoursBoard:
        approx = cv2.approxPolyDP(contourBoard, 0.01*cv2.arcLength(contourBoard, True), True)
        area = cv2.contourArea(contourBoard)
        if ((len(approx) > 0) & (area > 10)):
            contour_list_board.append(contourBoard)

    cv2.drawContours(chassisImg, contour_list_chassis, -1, (0,255,0), 2) # Draw picked contour chassis
    cv2.drawContours(boardImg, contour_list_board, -1, (0,255,0), 2) # Draw picked contour board

    calcCentroids(contour_list_chassis, contour_list_board)

### Centroid Calculations ###
# All centroid calculations use the picked contours #
def calcCentroids(contour_list_chassis, contour_list_board):
    for contours in contour_list_chassis:
        mChassis = cv2.moments(contours)
        cxC = int(mChassis['m10']/mChassis['m00']) #Centroid Calculation for x chassis
        cyC = int(mChassis['m01']/mChassis['m00']) #Centroid Calculation for y chassis
        cv2.circle(origPic, (cxC,cyC), 10, (255,0,0), -20) # Draws Centroid Chassis
        global centroidChassis
        centroidChassis = [cxC, cyC]

    for contours in contour_list_board:
        mBoard = cv2.moments(contours)
        cxB = int(mBoard['m10']/mBoard['m00']) #Centroid Calculation for x board
        cyB = int(mBoard['m01']/mBoard['m00']) #Centroid Calculation for y board
        cv2.circle(origPic, (cxB,cyB), 10, (0,0,255), -20) # Draws Centroid Board
        global centroidBoard
        centroidBoard = [cxB, cyB]

    ai(frame)

URL =  "http://" + sys.argv[1] + "/stream.mjpg"
stream = urllib.urlopen(URL)
bytes=''

# Create new thread to handle movement
if sys.argv[2] == 'onlyVision':
    pass
else:
    init(str(sys.argv[2])) # Inits robot after opening URL

def ai(img):
    n = network()

    n.addNode("chassisNode", 0)
    n.addNode("output", 0)

    n.inputToNode("chassisNode", 1)

    n.setOutputNodes(["output"])
    n.setInputNodes(["chassisNode"])

    n.connectEdge("output", "chassisNode", 1)

    n.step()
    print n.getOut()
    print centroidChassis
    cv2.imshow("Original", origPic)

while True:
    bytes+=stream.read(2048) # Normally 1024, doubled for 60FPS
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        global frame
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR) # Grabs frame from camera
        show_video(frame)
        if cv2.waitKey(1) ==27:
            exit(0)
