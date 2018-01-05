### testMyro ###

import sys
import myro
import numpy as np
import cv2

foo = cv2.imread('img.jpg')

cv2.imshow('window', foo)
foo2 = myro.makePicture('img.jpg')
myro.show(foo2)


cv2.waitKey(0)
cv2.destroyAllWindows()
