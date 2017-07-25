import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    # scaleFactor Parameter specifying how much the image size is reduced at each image scale.
	# minNeighbors Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w,y+h), color=(255,0,0), thickness=2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(image=roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img=roi_color, pt1=(ex,ey), pt2=(ex+ew,ey+eh), color=(0,255,0), thickness=2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
