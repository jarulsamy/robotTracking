### Usage: python findRobot.py IP_ADDRESS:PORT COMX
import cv2
import urllib
import numpy as np
import sys
import math
import time
import threading

from math import acos
from math import sqrt
from math import pi


# Initial Variable Decleration
pt = []
centroidChassis = []
centroidBoard = []

class movementThread(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

        #   from myro import * # Only import myro if sys needs it
    #
    # def angle_between(self, p1, p2):
    #     ang1 = np.arctan2(*p1[::-1])
    #     ang2 = np.arctan2(*p2[::-1])
    #     return np.rad2deg((ang1 - ang2) % (2 * np.pi))
    def calculateDistance(self, p0, p1):
        x = p0[0] - p1[0]
        y = p0[1] - p1[1]
        ret = math.sqrt((x ** 2) + (y ** 2))
        return ret

    def GetAngle(self,p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dX = x2 = x1
        dY = y2 - y1
        rads = math.atan2 (-dY, dX) #wrong for finding angle/declination?
        return math.degrees (rads)


    def dotproduct(self,v1, v2):
      return sum((a*b) for a, b in zip(v1, v2))

    def length(self,v):
      return math.sqrt(self.dotproduct(v, v))

    def angle(self,v1, v2):
      return math.acos(self.dotproduct(v1, v2) / (self.length(v1) * self.length(v2)))


    def run(self):
        while True:
            tupleCentroidBoard = tuple(centroidBoard)
            tuplePt = tuple(pt)
            if centroidBoard != [] and centroidChassis != [] and pt != []:
                # print self.length(pt)
                # chassisDistPoint = self.calculateDistance(centroidChassis, pt)
                # boardDistPoint = self.calculateDistance(centroidBoard, pt)
                # chassisDistBoard = self.calculateDistance(centroidChassis, centroidBoard)
                #
                # cosC = ((chassisDistPoint ** 2) - (boardDistPoint ** 2) + (chassisDistBoard ** 2)) / (2 * chassisDistPoint * boardDistPoint)
                # cosC = math.degrees(math.cos(cosC))
                # print cosC
                # angle = self.angle_between(pt, centroidBoard)
                self.calc = self.angle(pt, centroidBoard)
                self.calc = math.degrees(self.calc)
                print self.calc
                # if self.angle > 5:
                #     # turnBy(self.angle, "deg")
                #     pass
                # else:
                #     forward(.1,.1)

if len(sys.argv) != 3:
    print "Usage: %s <ip_address:port COMX>" % sys.argv[0]
    sys.exit(-1)

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global pt
        pt = [x, y]
        px = frame[x,y]
        print px
    return pt

def show_video(jpg):
    redUpper = np.array([230, 255, 200], dtype=np.uint8) # Upper threshold for chassis ID # HSV VERSION
    redLower = np.array([0, 120, 0], dtype=np.uint8) #Lower threshold for chassis ID # fail VERSION

    greenUpper = np.array([255, 100, 255], dtype=np.uint8) # Upper threshold for board ID
    greenLower = np.array([100, 70, 0], dtype=np.uint8) # Lower threshold for board ID
    # greenUpper = np.array([150, 130, 150], dtype=np.uint8) # Upper threshold for board ID
    # greenLower = np.array([40, 30, 80], dtype=np.uint8) # Lower threshold for board ID

    kernel = np.ones((5,5), np.uint8)

    readColors = jpg

    global origPic, chassisImg, boardImg
    origPic = readColors # Keeps an original unedited
    # YUV and LUV Work really well here, currenty sets everything robot to white
    chassisImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2LUV) #Converts to LUV for chassis detection
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

    # Keep the mouse click even through frame updates
    if pt == []:
        cv2.imshow('Original', origPic)
    else:
        cv2.circle(origPic, (pt[0], pt[1]), 5,  (0, 255, 0), -1)
        # tupleCentroidChassis = tuple(centroidChassis)
        # tupleCentroidBoard = tuple(centroidBoard)
        # tuplePt = tuple(pt)
        cv2.line(frame, tuple(centroidBoard), tuple(pt), (255, 0, 0), 5)
        cv2.line(frame, tuple(centroidChassis), tuple(pt), (255, 0, 0), 5)
        cv2.imshow("Original", origPic)

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


URL =  "http://" + sys.argv[1] + "/stream.mjpg"
stream = urllib.urlopen(URL)
bytes=''

# Create new thread to handle movement


moveThread = movementThread(1, 'movement') # Creates new thread based on ID: 1 and Name: movement
moveThread.daemon = True # Closes thread if main thread is closed
moveThread.start() # Starts thread ONCE should never be in loop

if sys.argv[2] == 'onlyVision':
    pass
else:
    from myro import *
    init(str(sys.argv[2])) # Inits robot after opening URL
    setAngle(0)

while True:
    bytes+=stream.read(2048) # Normally 1024, doubled for 60FPS
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        global frame
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR) # Grabs frame from camera
        show_video(frame) # Passing each frame to show_video function


        cv2.imshow('Original', frame)
        cv2.imshow('Chassis Image', chassisImg)
        cv2.imshow('Board Image', boardImg)
        cv2.namedWindow("Original")
        cv2.setMouseCallback("Original", click) # Calls click() when original picture is clicked on
        if cv2.waitKey(1) ==27:
            from myro import stop
            stop()
            exit(0)
