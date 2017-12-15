### Learning Classes ###

import sys

import cv2
import numpy as np

class robotTracking(object):

    def __init__(self, img):
        self.img = img

    def show_img(self):
        cv2.imshow('foo', self.img)
        cv2.waitKey(0)

    def findContours(self):
        
img = cv2.imread('img.jpg')
jeff = robotTracking(cv2.imread('img.jpg'))
jeff.show_img()
