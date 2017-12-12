### PRINTS COLOR SPACES IN CV2 ###
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags
