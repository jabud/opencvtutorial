import cv2
import numpy as np

# read image
img = cv2.imread('images/jorge.jpg', cv2.IMREAD_COLOR)

# Now, we can reference specific pixels, like so:
px = img[55,55]

# Next, we could actually change a pixel:
img[55,55] = [255,255,255]

# Then re-reference:
px = img[55,55]

print(px)

#We can reference an ROI, or Region of Image, like so:
px = img[400:650,100:350]
print(px)
# We can also modify the ROI, like this:
img[100:150,100:150] = [255,255,255]
# We can reference certain characteristics of our image:
print(img.shape)
print(img.size)
print(img.dtype)

# And we can perform operations, like:
x1 = 580
x2 = 700
y1 = 240
y2 = 325
watch_face = img[y1:y2, x1:x2]
img[0:(y2-y1),0:(x2-x1)] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
