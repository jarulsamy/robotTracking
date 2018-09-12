import cv2
from pyzbar.pyzbar import decode

URL = "http://10.0.0.101:8000/stream.mjpg"
cap = cv2.VideoCapture(URL)

while True:
    ret, frame = cap.read()
    qr = decode(frame)
    for obj in qr:
        poly = (obj.polygon)
        cv2.rectangle(frame, poly[0], poly[2], (255, 0, 0), 3)
    cv2.imshow("img", frame)
    
    if cv2.waitKey(1) == 27:
        exit(0)