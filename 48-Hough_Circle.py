import cv2
import numpy as np

img1 = cv2.imread("coins.jpg")
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
blur1 = cv2.medianBlur(gray1,5)
circles = cv2.HoughCircles(blur1,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4 , param1=200,param2=10,minRadius=15, maxRadius=90)  

#1:çözünürlük,çemberler arası min mesafe: img1.shape[0]/64
#param1=200 = gradient değeri ,param2=10 = threshold değeri metoda özeldir doğrudan girilir.
#minRadius=5, maxRadius=30 çemberlerin tahmin ettiğimiz yarıçap değerleri

if circles is not None: 
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow("circles",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



