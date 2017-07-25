import cv2
import numpy as np

img = cv2.imread('images/bookpage.jpg')
# setting threshold                    THR VAL   FUNCT_APPLY
retval, threshold = cv2.threshold(src=img, thresh=12, maxval=255, type=cv2.THRESH_BINARY)
# gray scale
grayscaled = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# adapted BLCKSIZE=size of pixel neighborhood to calc thr, C=Constant subtracted from the mean
th = cv2.adaptiveThreshold(src=grayscaled, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
							thresholdType=cv2.THRESH_BINARY, blockSize=115, C=1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('adapted', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
