import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    # take the double derivative of intensity to detect edges == 0
    laplacian = cv2.Laplacian(src=frame, ddepth=cv2.CV_64F, borderType=cv2.BORDER_REFLECT)
    # derivative over x axis
    sobelx = cv2.Sobel(src=frame, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
    # derivative over y axis
    sobely = cv2.Sobel(src=frame, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
    # Get magnitude and direction of gradients to draw the edge using thrsh
    edges = cv2.Canny(image=frame, threshold1=100, threshold2=300)

    # SHOW
    cv2.imshow('Original',frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('Sobel X', sobelx)
    cv2.imshow('Sobel Y', sobely)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
