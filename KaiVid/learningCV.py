from base.KaicongInput import KaicongInput
import cv2
import numpy as np

### Variables for click_and_crop ###
mousePoint = []
cropping = False
### Variables for click_and_crop ###


class KaicongVideo(KaicongInput):
    global maxContour, maxContourData
    maxContour = 0
    maxContourData = 0
    ### Mouse point Drawing ###
    def click_and_crop(event, x, y, flags, param):
    	global mousePoint, cropping
    	if event == cv2.EVENT_LBUTTONDOWN:
    		print('foo')
    		mousePoint = [(x, y)]
    		cropping = True
    		mousePoint.append((x, y))
    		cropping = False

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
        redLower = np.array([0, 0, 100], dtype=np.uint8) #Thresholds for robot ID
        #redUpper = np.array([120, 150, 255], dtype=np.uint8) #Thresholds for robot ID
        redUpper = np.array([120, 150, 255], dtype=np.uint8) #Thresholds for robot ID
        kernel = np.ones((5,5), np.uint8)

        readColors = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        origPic = readColors
        #HSV Works really well here, currenty sets everything red to white
        #Else set to black
        altColorSpaceImg = cv2.cvtColor(readColors, cv2.COLOR_BGR2YUV) #Converts to YUV

        blurredImg = cv2.GaussianBlur(altColorSpaceImg, (11, 11), 10) #Blurs image to deal with noise
        #blurredImg = cv2.medianBlur(blurredImg, 5) #Uses median blur to filter out even more noise
        blurredImg = cv2.bilateralFilter(blurredImg, 25, 75, 75) #Uses bilaterial filtering to deal with more noise
        ### Mask Stuff ###
        mask = cv2.inRange(blurredImg, redLower, redUpper)
    	mask = cv2.erode(mask, kernel, iterations=2)
    	mask = cv2.dilate(mask, kernel, iterations=2)
        ### Mask Stuff END ###

        ### Contour Stuff ###
        im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Find countour for masked image
        cnt = contours[0]
        cv2.drawContours(altColorSpaceImg, contours, -1, (0,0,255), 2) #Draw countours on ALT Image
        # Finds Largest blob

        for contour in contours:
            contourSize = cv2.contourArea(cnt)
            global maxContour
            if contourSize > maxContour:
                print('big')
                global maxContour, maxContourData
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
        cv2.imshow('Final',finalImage)
        cv2.imshow('Mask', mask)

        if mousePoint == []:
            cv2.imshow('Original', origPic)
        else:
            cv2.rectangle(origPic, mousePoint[0], mousePoint[1], (0, 255, 0), 10)
    	cv2.imshow("Original", origPic)
        ### Show Images END ###

        ### Centroid Calculations ###
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        firstCx = cx - 10
        firstCy = cy - 10
        secondCx = cx + 10
        secondCy = cy + 10
        #print(cx,firstCx, secondCx)
        #print(cx, secondCx, secondCy)
        cv2.rectangle(altColorSpaceImg, (firstCx,firstCy), (secondCx,secondCy), (255,0,0), 10)
        cv2.imshow('Alternative Color Space Image', altColorSpaceImg)
        # Note: waitKey() actually pushes the image out to screen
        if cv2.waitKey(1) ==27:
            exit(0)

    video = KaicongVideo(sys.argv[1], show_video)
    video.run()
