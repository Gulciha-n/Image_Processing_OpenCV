import cv2
import numpy as np

cap  = cv2.VideoCapture("dog.mp4")

while True:
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #nesnelerin izini sürmek için hsv dönüşümü yapıyoruz.
    sensitivity = 15 # beyaz renk ayrımı için kullanacağız
    lower_white = np.array([0,0,255-sensitivity]) # beyaz renkler için en düşük bir hsv aralığı belilrledik. (hsv code for white)
    upper_white = np.array([255,sensitivity,255]) # beyaz renkler için en düşük bir hsv aralığı belilrledik.
    
    mask = cv2.inRange(hsv ,lower_white, upper_white ) # lower ve upper olan yere maske uygula geri kalanı sil
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()


