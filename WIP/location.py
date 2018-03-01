import numpy as np
import cv2

origPic = np.zeros((600,400,3), np.uint8)


pt = [250, 300] # Green
centroidChassis = [200, 200] # Red
centroidBoard = [100, 100]

cv2.circle(origPic, (pt[0], pt[1]), 5,  (0, 255, 0), -1) #GREEN
cv2.circle(origPic, (centroidChassis[0], centroidChassis[1]), 5,  (0, 0, 255), -1) #RED

cv2.imshow('original', origPic)

def pointLocation(centroidChassis, centroidBoard, pt):
    if centroidChassis == [] or centroidBoard == [] or pt == []:
        return "Either centroidChassis or centroidBoard is undefined"
    else:
        xDist = abs(centroidChassis[0] - pt[0])
        yDist = abs(centroidChassis[1] - pt[1])
    if pt[0] > centroidChassis[0] and xDist > yDist:
        return 'right'
    if pt[0] < centroidChassis[0] and xDist > yDist:
        return 'left'
    if pt[1] > centroidChassis[1] and yDist > xDist:
        return 'down'
    if pt[1] < centroidChassis[1] and yDist > xDist:
        return 'up'
print pointLocation(centroidChassis, centroidBoard, pt)
cv2.waitKey(0)
cv2.destroyAllWindows()
