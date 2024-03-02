import cv2
import numpy as np

img = cv2.imread("map.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
_,thresh = cv2.threshold(blur,30,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
hull = [] #bulduğum contour noktalarını tutmak için bir liste hazırladım

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i]))
    cv2.drawContours(img,contours,-1,(0,0,255),2)
    cv2.drawContours(img,hull,-1,(255,0,0),2) # Tüm convex hull'ları çiz, mavi renkte, kalınlığı 2

cv2.imshow("image",img)
cv2.imshow("gray",gray)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

