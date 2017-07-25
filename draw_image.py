import cv2
import numpy as np

img = cv2.imread('images/jorge.jpg', 1)

# DRAW
# line         START      END       B,G,R   WIDTH
cv2.line(img=img, pt1=(400, 100), pt2=(500, 600), color=(0,0,255), thickness=15)
# rectangle          START      END       B,G,R   WIDTH
cv2.rectangle(img=img, pt1=(500,100), pt2=(900,600), color=(0,255,0), thickness=5)
# circle         CENTER    RAD   B,G,R    WIDTH
cv2.circle(img=img, center=(700,350), radius=200, color=(255,0,0), thickness=6)
# polygon points
pts = np.array([[400, 100], [500,30], [700,200], [1000,500]], np.int32)
#               ARRAY  CONECT i-f_POINTS B,G,R WIDTH
cv2.polylines(img=img, pts=[pts], isClosed=True, color=(255,255,0), thickness=4)

# WRITE
# select font
font = cv2.FONT_HERSHEY_SIMPLEX
#                 TEXT  Bottom_left_corner  FONT SIZE  B,G,R  SPACING  linetype
cv2.putText(img=img, text='Opencv Tutorial!', org=(500,700), fontFace=font, 
			fontScale=1, color=(0,255,255), thickness=2, lineType=cv2.LINE_AA)

# show image
cv2.imshow("image", img)
# listen to any key (0) to stop
cv2.waitKey(0)
# close window
cv2.destroyAllWindows()
