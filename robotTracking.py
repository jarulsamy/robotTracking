from base.KaicongInput import KaicongInput
import cv2
import numpy as np

class KaicongVideo(KaicongInput):

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
        redUpper = np.array([110, 150, 255], dtype=np.uint8)
        redLower = np.array([0, 0, 100], dtype=np.uint8)
        greenUpper = np.array([200, 200, 255], dtype=np.uint8)
        greenLower = np.array([0, 0, 150], dtype=np.uint8)
        kernel = np.ones((5,5), np.uint8)
        maxContourChassis = 0
        maxContourBoard = 0

        newImg = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR) # Each new frame
        orig = newImg # Saves each frame without changes

        chassis = cv2.cvtColor(newImg, cv2.COLOR_BGR2LUV)
        board = cv2.cvtColor(newImg, cv2.COLOR_BGR2XYZ)

        blurredChassis = cv2.GaussianBlur(chassis, (11, 11), 10) # Blurs image to deal with high-frequency noise
        blurredBoard = cv2.GaussianBlur(chassis, (11, 11), 10) # Blurs image to deal with high-frequency noise

        filteredChassis = cv2.bilateralFilter(blurredChassis, 25, 75, 75)
        filteredBoard = cv2.bilateralFilter(blurredBoard, 25, 75, 75)

        maskChassis = cv2.inRange(filteredChassis, redLower, redUpper)
        maskChassis = cv2.erode(maskChassis, kernel, iterations=2)
        maskChassis = cv2.dilate(maskChassis, kernel, iterations=2)

        maskBoard = cv2.inRange(filteredBoard, greenLower, greenUpper)
        maskBoard = cv2.erode(maskBoard, kernel, iterations=2)
        maskBoard = cv2.dilate(maskBoard, kernel, iterations=2)

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
            try:
                cntBoard = contoursBoard[0]
            except IndexError:
                return 'problems'

        cv2.drawContours(board, contoursBoard, -1, (0, 0, 255), 2)
        cv2.drawContours(chassis, contoursChassis, -1, (0, 0, 255), 2)

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

        cv2.imshow('Chassis Mask', maskChassis)
        cv2.imshow('Chassis Image', chassis)
        # cv2.imshow('Board Image', boardImg)
        if cv2.waitKey(1) ==27:
            exit(0)
            
video = KaicongVideo(sys.argv[1], show_video)
video.run()
