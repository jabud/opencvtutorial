import cv2
import numpy as np

# read image 
img_bgr = cv2.imread('images/im.jpg')
# gray scale for operations
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
# load templates
template_1 = cv2.imread('images/lalo.png', 0)
template_2 = cv2.imread('images/marce.png', 0)
# get width and height of template
w1, h1 = template_1.shape[::-1]
w2, h2 = template_2.shape[::-1]
# get an array with intensity values, the greater is the better match
res1 = cv2.matchTemplate(image=img_gray, templ=template_1, method=cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(image=img_gray, templ=template_2, method=cv2.TM_CCOEFF_NORMED)
# find the coordinates where intensity greater than threshold
loc1 = np.where(res1 >= 0.9)
loc2 = np.where(res2 >= 0.9)
# draw a rectangle where the match was found!
for pt1 in zip(*loc1[::-1]):
    cv2.rectangle(img=img_bgr, pt1=pt1, pt2=(pt1[0] + w1, pt1[1] + h1), color=(0,255,0), thickness=2)

for pt2 in zip(*loc2[::-1]):
    cv2.rectangle(img=img_bgr, pt1=pt2, pt2=(pt2[0] + w2, pt2[1] + h2), color=(0,255,0), thickness=2)

cv2.imshow('Detected',img_bgr)
# cv2.imshow('template', template)
# cv2.imshow('img_bgr', img_gray)

# listen to any key (0) to stop
cv2.waitKey(0)
# close window
cv2.destroyAllWindows()
