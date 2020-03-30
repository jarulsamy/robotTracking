import os
import threading
import time

import cv2
import numpy as np
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

import tensorflow as tf

# import sys
# from collections import defaultdict
# from io import StringIO

CWD_PATH = os.getcwd()
# MODEL_NAME = 'final'
PATH_TO_CKPT = "qr_graph.pb"
PATH_TO_LABELS = "object-detection.pbtxt"

NUM_CLASSES = 2


class imageThread(threading.Thread):
    def __init__(self, threadID, name, URL):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = URL
        self.cap = cv2.VideoCapture(URL)

    def getFrame(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return frame


# Load Detection graph
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, "rb") as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name="")
# Load label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True
)
category_index = label_map_util.create_category_index(categories)

IMAGE_SIZE = (12, 8)

URL = "http://10.0.0.101:8000/stream.mjpg"
# Setup thread to grab / convert color spaces of images
imgThread = imageThread(1, "image", URL)
imgThread.daemon = True
imgThread.start()

### PERFORAMCNE TUNING ###
# config = tf.ConfigProto()
# config.intra_op_parallelism_threads = 4 # SHOULD ALWAYS BE SAME AS OMP
# config.inter_op_parallelism_threads = 4
# os.environ["OMP_NUM_THREADS"] = "4"
# os.environ["KMP_BLOCKTIME"] = "4"
# os.environ["KMP_SETTINGS"] = "1"
# os.environ["KMP_AFFINITY"] = "granularity=fine,verbose,compact,1,0"

with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        while True:
            startTime = time.time()
            image_np = imgThread.getFrame()  # Grab image

            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name("image_tensor:0")

            boxes = detection_graph.get_tensor_by_name("detection_boxes:0")
            scores = detection_graph.get_tensor_by_name("detection_scores:0")
            classes = detection_graph.get_tensor_by_name("detection_classes:0")
            num_detections = detection_graph.get_tensor_by_name("num_detections:0")

            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded},
            )

            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                min_score_thresh=0.5,
                line_thickness=5,
            )
            # print(boxes)
            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
            cv2.imshow("Detection", image_np)
            elapsedTime = time.time() - startTime
            print("Processing Time: {}".format(elapsedTime))
            if cv2.waitKey(1) == 27:
                exit(0)
