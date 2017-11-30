import sys
sys.path.insert(0, "C:\Python27\myro")
from myro import *
import cv2
import numpy as np

class img(object):

    def __init__(self):
        self.img = cv2.imread("colorTest.jpg")

    def showImage(self):
        cv2.imshow("image", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

run = img()
run.showImage()
