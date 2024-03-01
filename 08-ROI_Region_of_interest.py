import cv2
import numpy as np 
import matplotlib.pyplot as plt

path = "Football.png"
img = cv2.imread(path)

roi = img[0:300 , 400:650]
img[0:300 , 0:250] = roi

cv2.imshow("Football",img)
cv2.imshow("roi",roi)

print("image shape : {}".format(img.shape))

cv2.waitKey(0)
cv2.destroyAllWindows()

