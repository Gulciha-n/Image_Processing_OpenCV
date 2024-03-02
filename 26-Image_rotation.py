import cv2
import numpy as np

img = cv2.imread("filter.png",0)
row , column = img.shape


M = cv2.getRotationMatrix2D((row/2, column/2),90,1)   # parametreler  = satır,sütun,döndürme yönü,ölçek(1 kat,3kat vs)
dst = cv2.warpAffine(img,M,(column,row))

M2 = cv2.get
cv2.imshow("filter",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



