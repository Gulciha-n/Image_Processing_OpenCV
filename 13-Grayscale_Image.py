import cv2
import numpy as np

img = np.zeros((10,10) , np.uint8 )

img[0,0] = 255
img[0,1] = 200
img[0,2] = 100
img[0,3] = 50
img[0,4] = 10

# img[1,0] = 10
# img[1,1] = 50
# img[1,2] = 100
# img[1,3] = 200
# img[1,4] = 250

img = cv2.resize(img , (500,500) , interpolation=cv2.INTER_AREA)

cv2.imshow("Grayscale",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
