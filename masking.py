import cv2 as cv
import numpy as np
import warnings
warnings.simplefilter(action='ignore')

img = cv.imread('Images/bridge-small.jpg')
cv.imshow('Bridge', img)

print(img.shape)  # (427, 640, 3)  (height, width, color channels)

blank = np.zeros((img.shape[0], img.shape[1]), dtype='uint8')
cv.imshow("Blank Image", blank)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow("Circle", circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow("Rectangle", rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)