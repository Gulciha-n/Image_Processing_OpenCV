import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "sunset.jpg"
img = cv2.imread(path)
#print(img)
corner = img[0:300 , 0:400]  # [y,x]

img[0:300 , 0:400] = [255,0,0]

cv2.imshow("Sunset",img)
cv2.imshow("test_corner",corner)

cv2.waitKey(0) 
cv2.destroyAllWindows()

