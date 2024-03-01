# RGB ,BGR ,HSV, Grayscale

import cv2
import numpy as np

img = cv2.imread("clone.jpg")

#Convert BGR to RGB 
img_RGB= cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
img_HSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
img1_GRAY = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow("image BGR",img)
cv2.imshow("image RGB",img_RGB)
cv2.imshow("image HSV",img_HSV)
cv2.imshow("image GRAY",img1_GRAY)

cv2.waitKey(0)
cv2.destroyAllWindows()
