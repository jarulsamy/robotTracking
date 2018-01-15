import cv2
import numpy as np

Mat bw, img = imread("img.jpg");
cvtColor(img, bw, COLOR_BGR2GRAY);

threshold(bw, bw, 150, 255, CV_THRESH_BINARY);

// Find all the contours in the thresholded image
vector<vector<Point> > contours;
vector<Vec4i> hierarchy;
findContours(bw, contours, hierarchy, CV_RETR_LIST, CV_CHAIN_APPROX_NONE);
