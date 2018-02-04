from base.KaicongInput import KaicongInput
import cv2
import numpy as np
###
template1 = cv2.imread('temp.png')
#template2 = cv2.imread('temp.png')
#template3 = temp3.jpg
#template4 = temp4.jpg
#template5 = temp5.jpg
###

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

    if len(sys.argv) != 2:
        print "Usage: %s <ip_address>" % sys.argv[0]
        sys.exit(-1)

    def show_video(jpg):
        redLower = np.array([0, 0, 125], dtype=np.uint8)
        redUpper = np.array([30, 100, 255], dtype=np.uint8)

        # greenLower = np.array([0,50,10], dtype=np.uint8)
        # greenUpper = np.array([20,255,40], dtype=np.uint8)

        kernel = np.ones((5,5), np.uint8)

        img1 = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        #HSV Works really well here, currenty sets everything red to white
        #Else set to black
        img = cv2.cvtColor(img1, cv2.COLOR_BGR2YUV)

        blurred = cv2.GaussianBlur(img, (11, 11), 0)
        mask = cv2.inRange(blurred, redLower, redUpper)
    	mask = cv2.erode(mask, kernel, iterations=10)
    	mask = cv2.dilate(mask, kernel, iterations=10)
        cv2.imshow('i',mask)
        cv2.imshow('old', img)
        # Note: waitKey() actually pushes the image out to screen
        if cv2.waitKey(1) ==27:
            exit(0)

    video = KaicongVideo(sys.argv[1], show_video)
    video.run()
