from base.KaicongInput import KaicongInput
import cv2
import numpy as np

# Color space info:
# Good: YUV LUV YCR_CV
# Okay: HSV HLS LAB Most of these have issues with noise
# Bad: RGB BGR

### Variables for click_and_crop ###
mousePoint = []
boardPoint = []
cropping = False
ix, iy = -1, -1
### Variables for click_and_crop ###

class KaicongVideo(KaicongInput):
    ### Initial Variable Decleration ###
    global maxContourChassis, maxContourDataChassis, maxContourBoard, maxContourDataBoard, ix, iy
    maxContourChassis = 0
    maxContourDataChassis = 0
    maxContourBoard = 0
    maxContourDataBoard = 0
    ### Initial Variable Decleration ###

    ### Mouse point Drawing ###
    def click_and_crop(event, x, y, flags, param):
    	global mousePoint, cropping, boardPoints
    	if event == cv2.EVENT_LBUTTONDOWN:
    		mousePoint = [(x, y)]
    		cropping = True
    		mousePoint.append((x, y))
    		cropping = False

        if event == cv2.EVENT_RBUTTONDOWN:
            print 'Defined Board Position'
            boardPoint = [(x, y)]
            cropping = True
            boardPoint.append((x, y))
            cropping = False
            ix,iy = x,y
            print(boardPoint)

    cv2.namedWindow("Original")
    cv2.setMouseCallback("Original", click_and_crop)
    ### Mouse Point Drawing End ###

    PACKET_SIZE = 1024
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
    import numpy as np
    import cv2
    import sys

    if len(sys.argv) != 2:
        print "Usage: %s <ip_address>" % sys.argv[0]
        sys.exit(-1)

    def show_video(jpg):
        ### Defining Inital Necessary Variables ###
        redUpper = np.array([110, 150, 255], dtype=np.uint8) #Thresholds for chassis ID
        redLower = np.array([0, 0, 100], dtype=np.uint8) #Thresholds for chassis ID

        greenUpper = np.array([200, 200, 255], dtype=np.uint8) #Thresholds for board ID
        greenLower = np.array([0, 0, 150], dtype=np.uint8) #Thresholds for board ID

        #redUpper = np.array([120, 150, 255], dtype=np.uint8) #Thresholds for robot ID
        kernel = np.ones((5,5), np.uint8)

        readColors = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        origPic = readColors
        #YUV and LUV Work really well here, currenty sets everything robot to white
        #Else set to black
        chassisImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2LUV) #Converts to LUV for chassis detectionS
        boardImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2XYZ) # Converts to HLS for board detection

        blurredImgChassis = cv2.GaussianBlur(chassisImg, (11, 11), 10) #Blurs image to deal with noise
        blurredImgChassis = cv2.bilateralFilter(blurredImgChassis, 25, 75, 75) #Uses bilaterial filtering to deal with more noise

        blurredImgBoard = cv2.GaussianBlur(boardImg, (11, 11), 10) #Blurs image to deal with noise
        blurredImgBoard = cv2.bilateralFilter(blurredImgBoard, 25, 75, 75) #Uses bilaterial filtering to deal with more noise

        ### Mask Stuff ###
        maskChassis = cv2.inRange(blurredImgChassis, redLower, redUpper)
    	maskChassis = cv2.erode(maskChassis, kernel, iterations=2)
    	maskChassis = cv2.dilate(maskChassis, kernel, iterations=2)

        maskBoard = cv2.inRange(blurredImgBoard, greenLower, greenUpper)
    	maskBoard = cv2.erode(maskBoard, kernel, iterations=2)
    	maskBoard = cv2.dilate(maskBoard, kernel, iterations=2)
        ### Mask Stuff END ###

        ### Contour Stuff ###
        im2Chassis, contoursChassis, hierarchyChassis = cv2.findContours(maskChassis, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
        im2Board, contoursBoard, hierarchyBoard = cv2.findContours(maskBoard, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
        # Try catch for contour issues on other color spaces
        try:
            cntChassis = contoursChassis[1]
        except IndexError:
            cntChassis = contoursChassis[0]

        try:
            cntBoard = contoursBoard[1]
        except IndexError:
            cntBoard = contoursBoard[0]


        cv2.drawContours(chassisImg, contoursChassis, -1, (0,0,255), 2) #Draw countours on ALT Image
        cv2.drawContours(boardImg, contoursBoard, -1, (0,0,255), 2) #Draw countours on ALT Image
        # Finds Largest blob

        for contourChassis in contoursChassis:
            global maxContourChassis, contourSizeChassis, maxContourDataChassis
            contourSizeChassis = cv2.contourArea(cntChassis)
            if contourSizeChassis > maxContourChassis:
                maxContourChassis = contourSizeChassis
                maxContourDataChassis = contourChassis
            # Has issues if put togethor
        for contourBoard in contoursBoard:
            global maxContourBoard, contourSizeBoard, maxContourDataBoard
            contourSizeBoard = cv2.contourArea(cntBoard)
            if contourSizeBoard > maxContourBoard:
                maxContourBoard = contourSizeBoard
                maxContourDataBoard = contourBoard

        areaMaskChassis = np.zeros_like(maskChassis)
        areaMaskBoard = np.zeros_like(maskBoard)

        cv2.fillPoly(areaMaskChassis,[maxContourDataChassis],1) # Draws new areaMask onto new image
        cv2.fillPoly(areaMaskBoard,[maxContourDataBoard],1) # Draws new areaMask onto new image

        # Somewhat unnecessary and problomatic code, can be reworked in the future
        Rc,Gc,Bc = cv2.split(blurredImgChassis) #Splits image in to RGB Values
        Rb,Gb,Bb = cv2.split(blurredImgBoard) #Splits image in to RGB Values
        # Creates solid black image + mask
        finalImage = np.zeros_like(blurredImgChassis)
        finalImage[:,:,0] = np.multiply(Rc,areaMaskChassis)
        finalImage[:,:,1] = np.multiply(Gc,areaMaskChassis)
        finalImage[:,:,2] = np.multiply(Bc,areaMaskChassis)

        finalImage[:,:,0] = np.multiply(Rb,areaMaskBoard)
        finalImage[:,:,1] = np.multiply(Gb,areaMaskBoard)
        finalImage[:,:,2] = np.multiply(Bb,areaMaskBoard)
        # Contour Stuff End ###

        ### Show Images ###
        #cv2.imshow('Final',finalImage)
        cv2.imshow('Chassis Mask', maskChassis)
        cv2.imshow('Chassis Image', chassisImg)
        cv2.imshow('Board Image', boardImg)
        ### Show Images END ###

        ### Centroid Calculations ###

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



        mChassis = cv2.moments(cntChassis)
        mBoard = cv2.moments(cntBoard)
        cxC = int(mChassis['m10']/mChassis['m00'])
        cyC = int(mChassis['m01']/mChassis['m00'])

        cxB = int(mBoard['m10']/mBoard['m00'])
        cyB = int(mBoard['m01']/mBoard['m00'])
        # Centroid Range Chassis
        firstCxC = cxC - 10
        firstCyC = cyC - 10
        secondCxC = cxC + 10
        secondCyC= cyC + 10
        # Centroid Range Board
        firstCxB = cxB - 10
        firstCyB = cyB - 10
        secondCxB = cxB + 10
        secondCyB = cyB + 10
        # Draw Centorid
        cv2.rectangle(origPic, (firstCxC,firstCyC), (secondCxC,secondCyC), (255,0,0), -1) # Draws Centroid Chassis
        cv2.rectangle(origPic, (firstCxB,firstCyB), (secondCxB,secondCyB), (0,0,255), -1) # Draws Centroid Board

        # Note: waitKey() actually pushes the image out to screen
        if cv2.waitKey(1) ==27:
            exit(0)

    video = KaicongVideo(sys.argv[1], show_video)
    video.run()
