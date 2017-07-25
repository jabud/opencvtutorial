import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    # CONVERT to HSV arrange (its easier than RGB or BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Set a range of color H  S  V
    lower_red = np.array([0, 100, 113])
    upper_red = np.array([255, 255, 179])
    # create a kernel within the range of red, if true 1 else 0 (white and black)
    mask = cv2.inRange(src=hsv, lowerb=lower_red, upperb=upper_red)
    # AND operation to show only red
    res = cv2.bitwise_and(src1=frame, src2=frame, mask= mask)
    # kernel for filters 5x5
    # Using Structuring Element we can create different kernel shapes.
    kernel = np.ones((5,5),np.uint8)
    # Apply filters of erosion and dilation to our frame
    erosion = cv2.erode(frame, kernel, iterations = 1)
    dilation = cv2.dilate(frame, kernel, iterations = 1)

    # SHOW
    cv2.imshow('Original',frame)
    cv2.imshow('res', res)
    cv2.imshow('Mask',mask)
    cv2.imshow('Erosion',erosion)
    cv2.imshow('Dilation',dilation)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
