# import the necessary packages
import numpy as np
import argparse
import time
import cv2

MODEL_NAME = 'scribbler_graph_board_v3/'
PATH_TO_LABELS = 'object-detection.pbtxt'
PATH_TO_CKPT = '{}frozen_inference_graph.pb'.format(MODEL_NAME)

image = cv2.imread("download.jpg")
classes = ["chassis", "board"]

blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromTensorflow(PATH_TO_CKPT, PATH_TO_LABELS)

net.setInput(blob)
start = time.time()
preds = net.forward()
end = time.time()
print("[INFO] classification took {:.5} seconds".format(end - start))

# loop over the top-5 predictions and display them
for (i, idx) in enumerate(idxs):
	# draw the top prediction on the input image
	if i == 0:
		text = "Label: {}, {:.2f}%".format(classes[idx],
                                     preds[0][idx] * 100)
		cv2.putText(image, text, (5, 25),  cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 0, 255), 2)

	# display the predicted label + associated probability to the
	# console
	print("[INFO] {}. label: {}, probability: {:.5}".format(i + 1,
                                                         classes[idx], preds[0][idx]))

# display the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
