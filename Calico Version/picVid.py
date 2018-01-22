import sys
sys.path.insert(0, 'C:\Python27\myro')
from myro import *
from graphics import *
import numpy as np
import urllib
from colorsys import *



def newPic():
        urllib.urlretrieve("http://192.168.0.100:81/snapshot.cgi?loginuse=admin&loginpas=123456","img.jpg")
        global origPic
        origPic = makePicture("img.jpg")
"""
def robot(x):
    com = str(x)
    init(com)
"""

def findRobot():
    #Grabs New Image from link Above
    newPic()
    #Creates blank images in prep for blob, in theory takes less time
    chassisConvertedImg = (Picture(640, 480))
    boardConvertedImg = Picture(640, 480)
    chassisBlobPic = Picture(640, 480)
    boardBlobPic = Picture(640, 480)
    grid = Picture(origPic)
    #Empty lists / variables used for centroid data later
    blackPixelsChassis = []
    whitePixelsChassis = []
    blackPixelsBoard = []
    whitePixelsBoard = []
    xBlackChassis = 0
    yBlackChassis = 0
    xBlackBoard = 0
    yBlackBoard = 0
    #Values used by converter machines
    yiqValues = []
    yuvValues = []

	#Goes through all pixels to getRGB
    for x in range (origPic.width):
        for y in range(origPic.height):
            rgbValues = origPic.getRGB(x,y)
            yiqMachine(chassisConvertedImg, rgbValues[0],rgbValues[1],rgbValues[2], x, y)
            yuvMachine(boardConvertedImg, rgbValues[0],rgbValues[1],rgbValues[2], x, y)
            foundChassis = detectChassis(chassisConvertedImg, x, y)
            foundBoard = detectBoard(boardConvertedImg, x, y)
            #Sets Black Pixels for Chassis
            if foundChassis == True:
                chassisBlobPic.setRGB(x,y,0,0,0)
                blackPixelsChassis.append([x,y])
                xBlackChassis += x
                yBlackChassis += y
            #Sets Whtie Pixels for Chassis
            else:
                chassisBlobPic.setRGB(x,y,255,255,255)
                whitePixelsChassis.append([x,y])
            #Sets Black Pixels for Board
            if foundBoard == True:
               boardBlobPic.setRGB(x,y,0,0,0)
               blackPixelsBoard.append([x,y])
               xBlackBoard += x
               yBlackBoard += y
            #Sets White Pixels for Board
            else:
                boardBlobPic.setRGB(x,y,255,255,255)
                whitePixelsBoard.append([x,y])
    #Shows All Images
    show(origPic,"Original Image")
    #show(chassisConvertedImg, "Chassis Converted Image")
    #show(boardConvertedImg, "Board Converted Image")
    show(chassisBlobPic, "Chassis Blob Pic")
    show(boardBlobPic, "Board Blob Pic")
    show(grid, "Grid")
    #Attaches Handles to important windows to draw centroids
    chassisBlobWin = getWindow("Chassis Blob Pic")
    boardBlobWin = getWindow("Board Blob Pic")
    origImgWin = getWindow("Original Image")
    gridWin = getWindow("Grid")
    #Adds mouse monitoring code on grid window
    gridWin.onMouseDown(mouseDown)
    #Centroid Statistics
    try:
        #Centroid Stats Calculated Chassis
        xCentroidChassis = xBlackChassis / len(blackPixelsChassis)
        yCentroidChassis = yBlackChassis / len(blackPixelsChassis)
        #Centroid Stats Calculated Board
        xCentroidBoard = xBlackBoard / len(blackPixelsBoard)
        yCentroidBoard = yBlackBoard / len(blackPixelsBoard)
    #Not really necessary because undefined variable exception occurs anyway.
    except ZeroDivisionError:
        print("Zero Diviosn Error")

    global centroid
    centroid = [xCentroidChassis,yCentroidChassis,xCentroidBoard,yCentroidBoard]

    #Centroid Stats Printed Chassis
    print("AVERAGE X VALUE Chassis", xCentroidChassis)
    print("AVERAGE Y VALUE Chassis", yCentroidChassis)
    #Centroid Stats Printed Board
    print("AVERAGE X VALUE Board", xCentroidBoard)
    print("AVERAGE Y VALUE Board", yCentroidBoard)

    #Draws centroids on Blob Images
    chassisBlobWin.draw(Circle((xCentroidChassis, yCentroidChassis),5))
    boardBlobWin.draw(Circle((xCentroidBoard, yCentroidBoard),5))

    #Base work for circles around robot and board
    chassisMarker = Circle((xCentroidChassis, yCentroidChassis),60)
    boardMarker = Circle((xCentroidBoard, yCentroidBoard),60)
    chassisMarker.fill.alpha = 0
    boardMarker.fill.alpha= 0

    #Special bit for orig image and circle drawing
    boardMarkerOrig = Circle((xCentroidBoard, yCentroidBoard),20)
    boardMarkerOrig.fill.alpha = 0

    #Actually draw on Windows
    chassisMarker.draw(chassisBlobWin)
    boardMarker.draw(boardBlobWin)

    boardMarkerOrig.draw(origImgWin)
    chassisMarker.draw(origImgWin)

    boardMarkerOrig.draw(gridWin)
    chassisMarker.draw(gridWin)

    origImgWin.draw(Circle((xCentroidChassis, yCentroidChassis),5))
    origImgWin.draw(Circle((xCentroidBoard, yCentroidBoard),5))

    gridWin.draw(Circle((xCentroidChassis, yCentroidChassis),5))
    gridWin.draw(Circle((xCentroidBoard, yCentroidBoard),5))

    #Create Grid Lines
    gridWin.draw(Line((0,160),(640,160)))
    gridWin.draw(Line((0,320),(640,320)))
    gridWin.draw(Line((214,0),(214,640)))
    gridWin.draw(Line((421,0),(421,640)))
    try:
        hypMovement.oldMarker
    except NameError:
        print("First Run")

#Predominantly used with Chassis Detection
def yiqMachine(yiqImg, r, g, b, x, y):
    yiqValues = rgb_to_yiq(r,g,b)
    yiqImg.setRGB(x,y,yiqValues[0], yiqValues[1],yiqValues[2])

#Predominantly used with Board Detection
def yuvMachine(yuvImg, r, g, b, x, y):
    yuvValues = rgb2yuv(r,g,b)
    yuvImg.setRGB(x,y,yuvValues[0], yuvValues[1],yuvValues[2])

#Uses YIQ to see Chassis, works best with red. Predator Vision
def detectChassis(yiqImg, x, y):
    yiqPixel = yiqImg.getRGB(x,y)
    if yiqPixel[0] <= 175 and yiqPixel[1] >=20 and yiqPixel[2] <=150:
        return True
    else:
        return False

#Uses YUV to detect green.
def detectBoard(yuvImg, x, y):
    yuvPixel = yuvImg.getRGB(x,y)
    if yuvPixel[0] >= 150 and yuvPixel[1] >= 150 and yuvPixel[2] >= 100:
        return True
    else:
        return False

def orient():
    #orient.direction[Left, Right, Down, Up]
    orient.direction = [False, False, False, False]
    if centroid[2] <= centroid[0]:
        print("Board Facing Left")
        orient.direction[0] = True
    if centroid[2] >= centroid[0]:
        print("Board Facing Right")
        orient.direction[1] = True
    if centroid[3] >= centroid[1]:
        print("Board Facing Down")
        orient.direction[2] = True
    if centroid[3] <= centroid[1]:
       distanceCheck = hypot(centroid[0] - mouseDown.marker[0], centroid[1] - mouseDown.marker[1])
       if distanceCheck < 100:
          print("Board Facing Up")
       print(distanceCheck)
       orient.direction[3] = True
    #print(orient.direction)

def mouseDown(o, e):
    gridWin = getWindow("Grid")
    mouseDown.marker = [e.x, e.y]
    gridWin.draw(Circle((mouseDown.marker[0], mouseDown.marker[1]),5))
    oldMouse = [e.x, e.y]
    orient()
    angle()
    hypoMovement()

def hypoMovement():
    #Hypothetical Movement function, really just for testing mousedown things
    print("FOO")
    wait(2)
    oldMarker = mouseDown.marker
    findRobot()

def angle():
    x = mouseDown.marker[0] - centroid[2]
    absX = abs(x)
    y = mouseDown.marker[1] - centroid[3]
    absY = abs(y)
    #newAngle = degrees(atan(centroid[2] - mouseDown.marker[0]))
    newAngle = degrees(atan(y/x))
    print(newAngle)
    robotPosition()

def robotPosition():
    chassisToPoint = abs(hypot(centroid[0] - mouseDown.marker[0], centroid[1] - mouseDown.marker[1]))
    boardToPoint = abs(hypot(centroid[2] - mouseDown.marker[0], centroid[3] - mouseDown.marker[1]))
    if boardToPoint < chassisToPoint:
       print("Robot is facing point")
       facingPoint = True
    else:
        print("Robot is NOT facing point")
        facingPoint = False
    if centroid[0] < mouseDown.marker[0] and centroid[2] < mouseDown.marker[0]:
        print("Entire Robot is to left of click")
    if centroid[0] > mouseDown.marker[0] and centroid[2] > mouseDown.marker[0]:
        print("Entire Robot is to right of click")
print(absX)
