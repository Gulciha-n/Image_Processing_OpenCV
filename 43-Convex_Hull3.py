import cv2
import numpy as np

img = cv2.imread("map.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
_,thresh = cv2.threshold(blur,30,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
hull = []

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),dtype=np.uint8)  # 3 channal'a ve img boyutlarına sahip black ground 
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i]))
    cv2.drawContours(bg,contours,-1,(0,255,0),3)
    cv2.drawContours(bg,hull,-1,(0,0,255),3)

cv2.imshow("image",img)
cv2.imshow("gray",gray)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)
cv2.imshow("bg",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
