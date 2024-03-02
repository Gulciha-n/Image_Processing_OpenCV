import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((500,500),dtype=np.uint8) 
 
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
cv2.rectangle(img,(200,170),(350,200),(255,255,255),-1)

cv2.imshow("img",img)
plt.hist(img.ravel(),256,[0,256]) #histogramı çiz - img.ravel() ile görüntü tek boyutlu dizi haline getirilir.
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
