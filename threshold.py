import cv2
import numpy as np

img = cv2.imread('images/bookpage.jpg')
# setting threshold                    THR VAL   FUNCT_APPLY
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# gray scale
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# adapted                     IMG      MAX          THR                            THR      BLCKSIZE C
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('adapted', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
