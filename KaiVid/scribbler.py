import sys
sys.path.insert(0,'C:\Python27\myro')
from myro import *
import cv2
import numpy as np

class MyClass(object):



    def __init__(self):
        if type(sys.argv[1]) == int:
            port = int(sys.argv[1])
            print(port)
        else:
            print(port)
            port = "foo"

        if type(port) == int:
            com = "com"
            newPort = com + str(port)
            init(newPort)
        else:
            print("Already Initiated...")
    #        init('com'sys.argv[0])
        forward(1,1)
        backward(1,1)
a = MyClass()
