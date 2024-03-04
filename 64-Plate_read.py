import cv2
import numpy as np
import pytesseract
import imutils

img = cv2.imread("licence_plate (1).jpg")
img = cv2.resize(img,(640,480))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtered = cv2.bilateralFilter(gray,5,255,255)  # çap,sigma değerleri
edge = cv2.Canny(filtered,30,200)
contours = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print("contours : ",contours)

cnts = imutils.grab_contours(contours)
#print("cnts",cnts)

cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:10]  #alana göre sıralama yapar
#print("sorted contours : ", sorted)

screen = None
for a in cnts:
    epsilon = 0.018*cv2.arcLength(a,True) # yay uzunkuları , contour boşlukları
    approxs = cv2.approxPolyDP(a,epsilon,True)
    if len(approxs) == 4:
        screen = approxs
mask = np.zeros(gray.shape,np.uint8)
new_img = cv2.drawContours(mask,[screen],0,(255,255,255),-1) 
new_image = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("image",img)
cv2.imshow("gray image",gray)
cv2.imshow("filtered",filtered)
cv2.imshow("edge",edge)
cv2.imshow("Masked Image", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

