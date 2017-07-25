import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(src=hsv, lowerb=lower_red, upperb=upper_red)
    res = cv2.bitwise_and(src1=frame, src2=frame, mask= mask)
    # Helpful for cleaning noise:
    # kernel for average
    kernel = np.ones((15,15),np.float32)/225
    # Smooth averaging
    smoothed = cv2.filter2D(res,-1,kernel)
    # Gaussian blur (Normal distributed kernel)
    blur = cv2.GaussianBlur(src=frame, ksize=(15,15), sigmaX=1, borderType=2)
    # Median filter (sets middle value de median value of kernel)
    median = cv2.medianBlur(src=frame, ksize=15)

    cv2.imshow('Original',frame)
    cv2.imshow('Averaging',smoothed)
    cv2.imshow('Gaussian Blurring',blur)
    cv2.imshow('Median Blur',median)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
