import cv2
import numpy as np

img1 = cv2.imread("text.png")

gray = cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

''' 
cv2.goodFeaturesToTrack işlemi, piksel değerlerinin float32 türünde olduğu bir gri tonlu
görüntü üzerinde çalişir. İlk adimda, görüntü cv2.cvtColor işlemi ile gri tonlu hale getirilir,
ancak bu işlem sonucunda piksel değerleri genellikle uint8 (0 ile 255 arasinda tamsayi) türündedir. 
Ancak, cv2.goodFeaturesToTrack işlemi daha yüksek hassasiyete sahip float32 türü bekler.
'''
corners = cv2.goodFeaturesToTrack(gray,50,0.01 ,10 )  #  köşeleri tespit eder => gri renk tonu , köşe satısı , kalite değeri , min uzaklık
corners = np.int0(corners)
for corner in corners:
    x,y = corner.ravel()   # çok boyutlu diziyi tek boyutlu dizi haline getirir
    cv2.circle(img1, (x,y), 3 , (0,0,255) , -1)

cv2.imshow("corner",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


