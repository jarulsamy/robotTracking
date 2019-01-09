import numpy as np
import os
import sys
import tensorflow as tf

from collections import defaultdict
from io import StringIO

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

import cv2
import threading
import time

import platform

from myro import *

init("/dev/ttyS4")

CWD_PATH = os.getcwd()
MODEL_NAME = 'scribbler_graph_board_v3/'
PATH_TO_CKPT = '{}frozen_inference_graph.pb'.format(MODEL_NAME)
# PATH_TO_CKPT = '{}optimized.pb'.format(MODEL_NAME)
PATH_TO_LABELS = 'object-detection.pbtxt'

pt = []

centroidChassis = []
centroidBoard = []


NUM_CLASSES = 2

class imageThread(threading.Thread):

    def __init__(self, threadID, name, URL):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = URL
        self.cap = cv2.VideoCapture(URL)
        # self.cap = cv2.VideoCapture("stream.avi")
        # self.cap = cv2.VideoCapture(0)

    def getFrame(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        # print "Frames per second using: {0}".format(fps)
        return frame


class movementThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def orientRobot(self, centroidChassis, centroidBoard):
        # Even if one centroid is missing keep moving to potentially find it later
        if centroidChassis == [] or centroidBoard == []:
            return "One of the following is undefined: centroidChassis, centroidBoard, pt"
        else:
            # Calculate distance between chassis and board, little unnecessary, x
            xDist = abs(centroidChassis[0] - centroidBoard[0])
            # Calculate distance between chassis and board, little unnecessary, y
            yDist = abs(centroidChassis[1] - centroidBoard[1])
        if centroidChassis[0] > centroidBoard[0] and xDist > yDist:
            return 'left'
        elif centroidChassis[1] < centroidBoard[1] and yDist > xDist:
            return 'down'
        elif centroidChassis[0] < centroidBoard[0] and xDist > yDist:
            return 'right'
        elif centroidChassis[1] > centroidBoard[1] and yDist > xDist:
            return 'up'
        else:
            return 'failed orientation'

    # Determines where mouse click is vs robot chassis centroid #
    # Intuative Orientation Method #
    def pointLocation(self, centroidChassis, centroidBoard, pt):
        # If screen hasn't been clicked, don't move
        if centroidChassis == [] or centroidBoard == [] or pt == []:
            return "One of the following is undefined: centroidChassis, centroidBoard, pt"
        else:
            # Calculate distance between chassis and mouse click, x
            xDist = abs(centroidChassis[0] - pt[0])
            # Calculate distance between chassis and mouse click, y
            yDist = abs(centroidChassis[1] - pt[1])
        if pt[0] > centroidChassis[0] and xDist > yDist:
            return 'right'
        if pt[0] < centroidChassis[0] and xDist > yDist:
            return 'left'
        if pt[1] > centroidChassis[1] and yDist > xDist:
            return 'down'
        if pt[1] < centroidChassis[1] and yDist > xDist:
            return 'up'
        else:
            return 'failed comparison'

    def lookAtPoint(self):
        motors(0.1, -0.1)
        time.sleep(.1)
        stop()

    # Simple calculate distance function using Pythagoreum Theorum
    def calculateDistance(self, x1, y1, x2, y2):
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return dist

    def move(self):
        if self.boardDistPoint == self.chassisDistPoint:
            print('this should never happen, probably a centroid glitch')
        if self.robotDirection != self.robotVPoint:  # Turn until approx. face the clicked point
            # All of this is intuative movement code, that doesn't really work
            if centroidBoard[0] < pt[0]:
                motors(.1, -.1)
                time.sleep(.1)
            elif centroidBoard[0] > pt[0]:
                motors(-.1, .1)
                time.sleep(.1)
            elif centroidBoard[1] < pt[1]:
                motors(-.1, .1)
                time.sleep(.1)
            elif centroidBoard[1] > pt[1]:
                motors(.1, -.1)
                time.sleep(.1)
            else:
                stop()
                time.sleep(.1)
                forward(.1, .1)
        else:
            stop()
            time.sleep(.1)
            forward(.1, .1)

    def run(self):
        while True:
            while (centroidChassis != [] and centroidBoard != [] and pt != []):
                # Which direction is the robot facing
                self.robotDirection = self.orientRobot(
                    centroidChassis, centroidBoard)
                # Where is the robot vs the mouse click
                self.robotVPoint = self.pointLocation(
                    centroidChassis, centroidBoard, pt)
                self.chassisDistPoint = self.calculateDistance(
                    centroidChassis[0], centroidChassis[1], pt[0], pt[1])
                self.boardDistPoint = self.calculateDistance(
                    centroidBoard[0], centroidBoard[1], pt[0], pt[1])
                self.move()

                if pt != []:
                    if self.chassisDistPoint < 50:  # If statement to kill program after reaching a certain proximety to the point
                        stop()
                        exit(0)
# Load Detection graph
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

# Load label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

IMAGE_SIZE = (12, 8)

URL = "http://10.0.0.101:8000/stream.mjpg"
# URL = "stream.avi"

# Setup thread to grab / convert color spaces of images
imgThread = imageThread(1, 'image', URL)
imgThread.daemon = True
imgThread.start()

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global pt
        pt = [x, y]
    return pt

### PERFORAMCNE TUNING CPU ONLY###

threads = 2
print("Intel CPU Detected...")
print("Attempting to configure Intel MKL DNN...")
config = tf.ConfigProto()
config.intra_op_parallelism_threads = threads # SHOULD ALWAYS BE SAME AS OMP_NUM_THREADS
config.inter_op_parallelism_threads = threads
os.environ["OMP_NUM_THREADS"] = str(threads)
os.environ["KMP_BLOCKTIME"] = str(threads)
os.environ["KMP_SETTINGS"] = "0"
os.environ["KMP_AFFINITY"] = "granularity=fine,verbose,compact,1,0"
print("Successfully loaded Intel MKL Settings")

config = tf.ConfigProto()

moveThread = movementThread(1, "Movement")
moveThread.daemon = True
moveThread.start()

with detection_graph.as_default():
    with tf.Session(graph=detection_graph, config=config) as sess:
        while True:
            startTime = time.time()
            image_np = imgThread.getFrame() # Grab image

            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            (boxes, scores, classes, num_detections) = sess.run(
              [boxes, scores, classes, num_detections],
              feed_dict={image_tensor: image_np_expanded})

            height, width, channels = image_np.shape

            boxes = np.squeeze(boxes)
            classes = np.squeeze(classes)
            scores = np.squeeze(scores)

            vis_util.visualize_boxes_and_labels_on_image_array(
              image_np,
              np.squeeze(boxes),
              np.squeeze(classes).astype(np.int32),
              np.squeeze(scores),
              category_index,
              use_normalized_coordinates=True,
              min_score_thresh=.3,
              line_thickness=5)

            # Chassis Centroid
            new_scores = []
            for i in range(len(scores)):
                if scores[i] > .5:
                    new_scores.append(scores[i])

            if new_scores[0] > .5:
                box = tuple(boxes[0].tolist())
                yMin = box[0] * height
                xMin = box[1] * width
                yMax = box[2] * height
                xMax = box[3] * width

                xCenter = (xMax + xMin) / 2
                yCenter = (yMax + yMin) / 2

                xCenterChassis = int(xCenter)
                yCenterChassis = int(yCenter)

                cv2.circle(image_np, (xCenterChassis, yCenterChassis), 10,  (255, 0, 0), -1)
            
            # Board Calculations
            if len(new_scores) > 1:
                if new_scores[1] > .5:
                    box = tuple(boxes[1].tolist())
                    yMin = box[0] * height
                    xMin = box[1] * width
                    yMax = box[2] * height
                    xMax = box[3] * width

                    xCenter = (xMax + xMin) / 2
                    yCenter = (yMax + yMin) / 2

                    xCenterBoard = int(xCenter)
                    yCenterBoard = int(yCenter)

                    cv2.circle(image_np, (xCenterBoard, yCenterBoard), 10, (0, 0, 255), -1)

            try:
                global centroidChassis, centroidBoard
                centroidChassis = [xCenterChassis, yCenterChassis]
                centroidBoard = [xCenterBoard, yCenterBoard]
            except:
                pass

            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
            if pt == []:
                cv2.imshow('Detection', image_np)
            else:
                cv2.circle(image_np, (pt[0], pt[1]), 5,  (0, 255, 0), -1)
                cv2.line(image_np, (xCenterChassis, yCenterChassis), (pt[0], pt[1]), (255,0,0), 5)
                cv2.imshow("Detection", image_np)


            cv2.namedWindow("Detection")
            cv2.setMouseCallback("Detection", click)
            elapsedTime = time.time() - startTime
            # print("Processing Time: {}".format(elapsedTime))
            if cv2.waitKey(1) == 27:
                stop()
                exit(0)
