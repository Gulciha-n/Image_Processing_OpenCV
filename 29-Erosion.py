import cv2
import numpy as np

img = cv2.imread("photo1.jpg") 

kernel = np.ones((5,5),np.uint8)   # 1'lerden oluşan matrisi resim üzerine getirerek resmin bozulmasını sağlayacağız.
erosion = cv2.erode(img,kernel,iterations=2) 

cv2.imshow("image",img)
cv2.imshow("erosion",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

