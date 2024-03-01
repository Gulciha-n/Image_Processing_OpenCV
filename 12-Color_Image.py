import cv2
import numpy as np

img = np.zeros([10,10,3] , np.uint8)

img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,100)
img[0,3] = (255,255,50)
img[0,4] = (255,255,15)

img = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)

cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()
