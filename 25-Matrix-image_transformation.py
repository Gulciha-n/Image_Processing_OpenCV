import cv2
import numpy as np

img = cv2.imread("Helikopter.jpg",0)  # 0=grayscale
print(img.shape)
row , column = img.shape  # img.shape iki değişkene sahip satır ve sütun 
#transformasyon matrisi = bir nesnenin pozisyonunu, boyutunu veya yönelimini değiştirmek için kullanılır.

M = np.float32([[1,0,10] , [0,1,70]]) # x ekseninde 1 kat 10 birim öteleme, y ekseninde 1 kat 70 birim öteleme
M1= np.float32([[1,0,100],[0,1,200]]) # M = dönüşüm matrisi 
dst = cv2.warpAffine(img,M,(row,column))
dst1 = cv2.warpAffine(img,M1,(row,column))

cv2.imshow("helikopter", img)
cv2.imshow("dst",dst)
cv2.imshow("dst",dst1)

cv2.waitKey()
cv2.destroyAllWindows()


