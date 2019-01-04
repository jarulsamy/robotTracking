# import numpy as np
# import cv2
# import tensorflow as tf


# URL = "http://10.0.0.101:8000/stream.mjpg"
# cap = cv2.VideoCapture(URL)

# cvNet = cv2.dnn.readNetFromTensorflow('final.pb', 'config.pbtxt')

# while True:
#     ret, img = cap.read()
#     rows = img.shape[0]
#     cols = img.shape[1]
#     cvNet.setInput(cv2.dnn.blobFromImage(img, 1.0/127.5, (300, 300), (127.5, 127.5, 127.5), swapRB=True, crop=False))
#     cvOut = cv2Net.forward()

#     for detection in cv2Out[0,0,:,:]:
#         score = float(detection[2])
#         if score > 0.3:
#             left = detection[3] * cols
#             top = detection[4] * rows
#             right = detection[5] * cols
#             bottom = detection[6] * rows
#             cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)
#     cv2.imshow('img', img)
#     if cv2.waitKey(1) ==27:
#         exit(0)


import cv2 as cv

URL = "http://10.0.0.101:8000/stream.mjpg"
cap = cv.VideoCapture(URL)

cvNet = cv.dnn.readNetFromTensorflow('scribbler_graph_qr_v2/dnn.pb', 'graph.pbtxt')
while True:
    ret, img = cap.read()
    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv.dnn.blobFromImage(img, 1.0/127.5, (300, 300), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    cvOut = cvNet.forward()

    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        if score > 0.3:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

    cv.imshow('img', img)
    cv.waitKey()