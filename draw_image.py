import cv2
import numpy as np

img = cv2.imread('images/jorge.jpg', 1)

# DRAW
# line         START      END       B,G,R   WIDTH
cv2.line(img, (400, 100), (500, 600), (0,0,255), 15)
# rectangle          START      END       B,G,R   WIDTH
cv2.rectangle(img, (500,100), (900,600), (0,255,0), 5)
# circle         CENTER    RAD   B,G,R    WIDTH
cv2.circle(img, (700,350), 200, (255,0,0), 6)
# polygon
pts = np.array([[400, 100], [500,30], [700,200], [1000,500]], np.int32)
#               ARRAY  CONECT i-f_POINTS B,G,R WIDTH
cv2.polylines(img, [pts], True, (255,255,0), 4)

# WRITE
# select font
font = cv2.FONT_HERSHEY_SIMPLEX
#                 TEXT               START   FONT SIZE B,G,R   SPACING  ?
cv2.putText(img, 'Opencv Tutorial!', (500,700), font, 1, (0,255,255), 2, cv2.LINE_AA)

# show image
cv2.imshow("image", img)
# listen to any key (0) to stop
cv2.waitKey(0)
# close window
cv2.destroyAllWindows()
