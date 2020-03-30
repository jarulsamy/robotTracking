import os

import cv2 as cv
import numpy as np

import tensorflow as tf

CWD_PATH = os.getcwd()
MODEL_NAME = "scribbler_graph_board_v3/"
# PATH_TO_CKPT = '{}frozen_inference_graph.pb'.format(MODEL_NAME)
PATH_TO_CKPT = "{}opt_graph.pb".format(MODEL_NAME)
PATH_TO_LABELS = "object-detection.pbtxt"

cvNet = cv.dnn.readNetFromTensorflow(PATH_TO_CKPT, "graph.pbtxt")

img = cv.imread("example.jpg")
rows = img.shape[0]
cols = img.shape[1]
cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
cvOut = cvNet.forward()

for detection in cvOut[0, 0, :, :]:
    score = float(detection[2])
    if score > 0.3:
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv.rectangle(
            img,
            (int(left), int(top)),
            (int(right), int(bottom)),
            (23, 230, 210),
            thickness=2,
        )

cv.imshow("img", img)
cv.waitKey()
