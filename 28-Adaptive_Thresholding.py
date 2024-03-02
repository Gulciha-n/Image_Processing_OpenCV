import cv2
import numpy as np 


img= cv2.imread("photo1.jpg",0)
ret , th = cv2.threshold(img , 150 , 255 , cv2.THRESH_BINARY)

th1 = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# max = 255 (daha keskin sınırlarla ayrılır.sıfır dersek de her şey siyah olur. alabileceği maksimum değer 255 vermeliyiz ki keskin sınırlarla ayırabilsin.)

th2 = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY , 11,2)

cv2.imshow("image",img)
cv2.imshow("binary threshold",th)
cv2.imshow("Adaptive Threshold",th1)
cv2.imshow("Gaussian Threshold",th2)

cv2.waitKey(0)
cv2.destroyAllWindows()


