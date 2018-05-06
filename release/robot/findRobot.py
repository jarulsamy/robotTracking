### Usage: python findRobot.py IP_ADDRESS

from base.KaicongInput import KaicongInput
import socket
import sys
import numpy as np
import cv2
import math
import time

### Host and Port info for pipeline server ###
HOST = '127.0.0.1'
PORT = 10000
s = socket.socket()
s.connect((HOST, PORT)) # Comment me if no robot untested and may have some issues. Submit a pull request if there is a problem
# Initial Variable Decleration
pt = []
centroidChassis = []
centroidBoard = []

class KaicongVideo(KaicongInput):
    # PACKET_SIZE = 1024
    PACKET_SIZE = 2048 # Double size shouldn't affect anything
    URI = "http://%s:81/livestream.cgi?user=%s&pwd=%s&streamid=3&audio=1&filename="

    def __init__(self, domain, callback, user="admin", pwd="123456"):
        KaicongInput.__init__(
            self,
            callback,
            domain,
            KaicongVideo.URI,
            KaicongVideo.PACKET_SIZE,
            user,
            pwd
        )
        self.bytes = ''

    def handle(self, data):
        self.bytes += data
        a = self.bytes.find('\xff\xd8')
        b = self.bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = self.bytes[a:b+2]
            self.bytes = self.bytes[b+2:]
            return jpg

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage: %s <ip_address>" % sys.argv[0]
        sys.exit(-1)
    # Handles click on Original Picture
    def click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            global pt
            pt = [x, y]
        return pt

    def show_video(jpg):
        redUpper = np.array([100, 150, 255], dtype=np.uint8) # Upper threshold for chassis ID
        redLower = np.array([0, 0, 100], dtype=np.uint8) #Lower threshold for chassis ID

        greenUpper = np.array([255, 200, 100], dtype=np.uint8) # Upper threshold for board ID
        greenLower = np.array([100, 0, 0], dtype=np.uint8) # Lower threshold for board ID

        contour_list_chassis = [] # List of all the contours for chassis. Cleared every frame to prevent memory issues
        contour_list_board = [] # List of all the contours for board. Cleared every frame to prevent memory issues

        kernel = np.ones((5,5), np.uint8)

        # YUV and LUV Work really well here, currenty sets everything robot to white
        readColors = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR) # Reads each new frame for colors

        origPic = readColors # Keeps an original unedited
        chassisImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2LUV) #Converts to LUV for chassis detection
        boardImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2RGB) #Converts to LUV for chassis detection # This weird double line thing
        boardImg = cv2.cvtColor(boardImg, cv2.COLOR_RGB2BGR) #Converts to LUV for chassis detection # is to fix a bug

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

        im2Chassis, contoursChassis, hierarchyChassis = cv2.findContours(edgeChassis, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
        # im2Board, contoursBoard, hierarchyBoard = cv2.findContours(maskBoard, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
        im2Board, contoursBoard, hierarchyBoard = cv2.findContours(edgeBoard, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image

        cv2.drawContours(chassisImg, contoursChassis, -1, (0,0,255), 2) #Draw countours on alternate color space chassis image
        cv2.drawContours(boardImg, contoursBoard, -1, (0,0,255), 2) #Draw countours on alternate color space board image

        # Keep the mouse click even through frame updates
        if pt == []:
            cv2.imshow('Original', origPic)
        else:
            cv2.circle(origPic, (pt[0], pt[1]), 5,  (0, 255, 0), -1)
            cv2.imshow("Original", origPic)

        # Elegant solution to combine color and shape detection for chassis. Looks for most circular contour
        for contourChassis in contoursChassis:
            approx = cv2.approxPolyDP(contourChassis, 0.01*cv2.arcLength(contourChassis, True), True)
            area = cv2.contourArea(contourChassis)
            if ((len(approx) > 8) & (area > 1000)):
                contour_list_chassis.append(contourChassis)

        # Elegant solution to combine color and shape detection for board. Looks for most rectangular contour
        for contourBoard in contoursBoard:
            approx = cv2.approxPolyDP(contourBoard, 0.01*cv2.arcLength(contourBoard, True), True)
            area = cv2.contourArea(contourBoard)
            if ((len(approx) > 0) & (area > 10)):
                contour_list_board.append(contourBoard)

        cv2.drawContours(chassisImg, contour_list_chassis, -1, (0,255,0), 2) # Draw picked contour chassis
        cv2.drawContours(boardImg, contour_list_board, -1, (0,255,0), 2) # Draw picked contour board

        ### Centroid Calculations ###
        # All centroid calculations use the picked contours #
        for contours in contour_list_chassis:
            mChassis = cv2.moments(contours)
            global cxC, cyC
            cxC = int(mChassis['m10']/mChassis['m00'])
            cyC = int(mChassis['m01']/mChassis['m00'])
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

        ### Orientation ###
        # Determines which way the robot is facing based on board centroid and chassis centroid #
        # Intuative Orientation method #
        def orientRobot(centroidChassis, centroidBoard):
            # Even if one centroid is missing keep moving to potentially find it later
            if centroidChassis == [] or centroidBoard == []:
                return "One of the following is undefined: centroidChassis, centroidBoard, pt"
            else:
                xDist = abs(centroidChassis[0] - centroidBoard[0]) # Calculate distance between chassis and board, little unnecessary, x
                yDist = abs(centroidChassis[1] - centroidBoard[1]) # Calculate distance between chassis and board, little unnecessary, y
            if centroidChassis[0] > centroidBoard[0] and xDist > yDist:
                return 'left'
            elif centroidChassis[1] < centroidBoard[1] and yDist > xDist:
                return 'down'
            elif centroidChassis[0] < centroidBoard[0] and xDist > yDist:
                return 'right'
            elif centroidChassis[1] > centroidBoard[1] and yDist > xDist:
                return 'up'
            else:
                return 'failed orientation'

        # Determines where mouse click is vs robot chassis centroid #
        # Intuative Orientation Method #
        def pointLocation(centroidChassis, centroidBoard, pt):
            # If screen hasn't been clicked, don't move
            if centroidChassis == [] or centroidBoard == [] or pt == []:
                return "One of the following is undefined: centroidChassis, centroidBoard, pt"
            else:
                xDist = abs(centroidChassis[0] - pt[0]) # Calculate distance between chassis and mouse click, x
                yDist = abs(centroidChassis[1] - pt[1]) # Calculate distance between chassis and mouse click, y
            if pt[0] > centroidChassis[0] and xDist > yDist:
                return 'right'
            if pt[0] < centroidChassis[0] and xDist > yDist:
                return 'left'
            if pt[1] > centroidChassis[1] and yDist > xDist:
                return 'down'
            if pt[1] < centroidChassis[1] and yDist > xDist:
                return 'up'
            else:
                return 'failed comparison'

        robotDirection = orientRobot(centroidChassis, centroidBoard) # Which direction is the robot facing
        robotVPoint = pointLocation(centroidChassis, centroidBoard, pt) # Where is the robot vs the mouse click

        # Simple calculate distance function using Pythagoreum Theorum
        def calculateDistance(x1,y1,x2,y2):
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return dist

        ### Movement / Sending to Robot ###
        def lookAtPoint(facing):
            if facing == False:
                s.send('motors(0.1, -0.1)')
                time.sleep(.05)
                s.send('stop')

        if pt != [] and centroidChassis != [] and centroidBoard != []:
            # If all three items are defined, keep doing calculations. Else: Keep moving a little bit to hopefully reobtain the centroid
            chassisDistPoint = calculateDistance(centroidChassis[0], centroidChassis[1], pt[0], pt[1])
            boardDistPoint = calculateDistance(centroidBoard[0], centroidBoard[1], pt[0], pt[1])

        if pt != []:
            if chassisDistPoint < 50: # If statement to kill program after reaching a certain proximety to the point
                # break
                s.send("stop()")
                sys.exit()
                return 'end'
            # Kind of unnecessary but will be added on to in the future
            if boardDistPoint == chassisDistPoint:
                print 'this should never happen, probably a centroid glitch'
            if robotDirection != robotVPoint: # Turn until approx. face the clicked point
                lookAtPoint(False)
                if centroidBoard[0] > pt[0]: # All of this is intuative movement code, that doesn't really work
                    s.send('motors(-.1, .1)')
                    time.sleep(.05)
                elif centroidBoard[0] < pt[0]:
                    s.send('motors(.1, -.1)')
                    time.sleep(.05)
                elif centroidBoard[1] > pt[1]:
                    s.send('motors(-.1, .1)')
                    time.sleep(.05)
                elif centroidBoard[1] < pt[1]:
                    s.send('motors(.1, -.1)')
                    time.sleep(.05)
                else:
                    s.send('stop()')
                    time.sleep(.05)
                    s.send('forward(.1,.1)')
            else:
                s.send('stop()')
                time.sleep(.05)
                s.send('forward(.1,.1)')

        # Show all the images / update all the images
        cv2.imshow('Original', origPic)
        cv2.imshow('Chassis Image', chassisImg)
        cv2.imshow('Board Image', boardImg)
        cv2.imshow('Blurred Board Image', blurredImgBoard)
        #
        def goToPoint(click):
            click = click[0]
            x = click[0]
            y = click[1]
            print(x, y)
            s.send("turnLeft(1,1)")

        def click_and_crop(event, x, y, flags, param):
            global mousePoint, cropping
            if event == cv2.EVENT_LBUTTONUP:
                mousePoint = [(x, y)]
                mousePoint.append((x, y))
                goToPoint(mousePoint)

        cv2.namedWindow("Original")
        cv2.setMouseCallback("Original", click_and_crop)

        if cv2.waitKey(1) == 27: # Close the windows and kill the program with Esc Key
            s.send("stop()")
            s.close()
            exit(0)

    video = KaicongVideo(sys.argv[1], show_video)
    cv2.namedWindow("Original")
    cv2.setMouseCallback("Original", click) # Calls click() when original picture is clicked on
    video.run()