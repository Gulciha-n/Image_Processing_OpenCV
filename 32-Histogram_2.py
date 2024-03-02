import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("smile.jpg")

cv2.imshow("smile",img)
plt.hist(img.ravel() , 256 , [0,256] ) 

cv2.waitKey(0)
cv2.destroyAllWindows()



