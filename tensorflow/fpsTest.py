import cv2

v = cv2.VideoCapture("http://10.0.0.101:8000/stream.mjpg")
ret, frame = v.read()

while True:
    ret, frame = v.read()
    cv2.imshow("img", frame)
    fps = v.get(cv2.CAP_PROP_FPS)
    print "Frames per second using: {0}".format(fps)
    if cv2.waitKey(1) == 27:
        exit(0)
