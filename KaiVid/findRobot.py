from base.KaicongInput import KaicongInput
import socket
import sys
import numpy as np
import cv2

# Color space info:
# Good: YUV LUV YCR_CV
# Okay: HSV HLS LAB Most of these have issues with noise
# Bad: RGB BGR


HOST = '127.0.0.1'
PORT = 10000
s = socket.socket()
# s.connect((HOST, PORT))


### Variables for click_and_crop ###
mousePoint = []
boardPoint = []
cropping = False
ix, iy = -1, -1
### Variables for click_and_crop ###

class KaicongVideo(KaicongInput):
    ### Initial Variable Decleration ###
    global maxContourChassis, maxContourDataChassis, maxContourBoard, maxContourDataBoard
    maxContourChassis = 0
    maxContourDataChassis = 0
    maxContourBoard = 0
    maxContourDataBoard = 0
    ### Initial Variable Decleration ###

    # PACKET_SIZE = 1024
    PACKET_SIZE = 2048
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

    def show_video(jpg):
        ### Defining Thresholds ###
        redUpper = np.array([100, 150, 255], dtype=np.uint8) #Thresholds for chassis ID
        redLower = np.array([0, 0, 100], dtype=np.uint8) #Thresholds for chassis ID

        greenUpper = np.array([255, 50, 100], dtype=np.uint8) #Thresholds for board ID
        greenLower = np.array([50, 0, 0], dtype=np.uint8) #Thresholds for board ID

        kernel = np.ones((5,5), np.uint8)

        # YUV and LUV Work really well here, currenty sets everything robot to white
        # Else set to black
        readColors = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR) # Each new frame

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

        edgeChassis = cv2.Canny(maskChassis, 75, 200)
        edgeBoard = cv2.Canny(maskBoard, 75, 200)

        im2Chassis, contoursChassis, hierarchyChassis = cv2.findContours(edgeChassis, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
        im2Board, contoursBoard, hierarchyBoard = cv2.findContours(edgeBoard, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image

        cv2.drawContours(chassisImg, contoursChassis, -1, (0,0,255), 2) #Draw countours on ALT Image
        cv2.drawContours(boardImg, contoursBoard, -1, (0,0,255), 2) #Draw countours on ALT Image

        if mousePoint == []:
            cv2.imshow('Original', origPic)
        else:
            cv2.rectangle(origPic, mousePoint[0], mousePoint[1], (0, 255, 0), 10)
            cv2.imshow("Original", origPic)

        if boardPoint == []:
            cv2.imshow('Original', origPic)
        else:
            cv2.rectangle(origPic, boardPoint[0], boardPoint[1], (0, 255, 0), 10)
            cv2.imshow("Original", origPic)

        contour_list_chassis = []
        contour_list_board = []
        # Much more elegant solution to grab largest blob / most circular blob
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

        cv2.drawContours(chassisImg, contour_list_chassis, -1, (0,255,0), 2)
        cv2.drawContours(boardImg, contour_list_board, -1, (0,255,0), 2)

        # if (len(contour_list_chassis) > 1): # Memory management so list doesn't get so big and crash
        #     contour_list_chassis = contour_list_chassis[0]
        # if (len(contour_list_board) > 1): # Memory management so list doesn't get so big and crash
        #     contour_list_board = contour_list_board[0]

        for contours in contour_list_chassis:
            global cxC, cyC
            mChassis = cv2.moments(contours)
            cxC = int(mChassis['m10']/mChassis['m00'])
            cyC = int(mChassis['m01']/mChassis['m00'])
            cv2.circle(origPic, (cxC,cyC), 10, (255,0,0), -20) # Draws Centroid Chassis

        for contours in contour_list_board:
            mBoard = cv2.moments(contours)
            global cxB, cyB
            cxB = int(mBoard['m10']/mBoard['m00'])
            cyB = int(mBoard['m01']/mBoard['m00'])
            cv2.circle(origPic, (cxB,cyB), 10, (255,0,0), -20) # Draws Centroid Board

        # Draw Centorid
        cv2.imshow('Original', origPic)
        cv2.imshow('Chassis Image', chassisImg)
        cv2.imshow('Blurred Chassis Image', blurredImgChassis)
        cv2.imshow('Board Image', boardImg)
        cv2.imshow('Blurred Board Image', blurredImgBoard)

        # def goToPoint(click):
        #     click = click[0]
        #     x = click[0]
        #     y = click[1]
        #     s.send("turnLeft(1,1)")

        def click_and_crop(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONUP:
                mousePoint = [(x, y)]
                cropping = True
                mousePoint.append((x, y))
                cropping = False
                goToPoint(mousePoint)

        cv2.namedWindow("Original")
        cv2.setMouseCallback("Original", click_and_crop)

        if cv2.waitKey(1) == 27:
            s.close()
            exit(0)

    video = KaicongVideo(sys.argv[1], show_video)
    video.run()
