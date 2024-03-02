import cv2
import numpy as np

img = cv2.imread("Helikopter.jpg",0)

kernel = np.ones((7,7),dtype=np.uint8)
dilation = cv2.dilate(img,kernel,iterations=1)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) #resimdeki gürültüleri azaltır
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel) # resimdeki uyumsuzluklar giderilir
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel) # resmi çerçeve olarak çizer
tophad = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

cv2.imshow("image",img) 
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing) 
cv2.imshow("gradient",gradient) 
cv2.imshow("tophat",tophad) 

cv2.waitKey(0)
cv2.destroyAllWindows()


