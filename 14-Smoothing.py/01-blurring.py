import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")


#blurring = reduce detail
#Blur images with various low pass filters
img = cv2.imread("NYC.jpg")

#convert BGR to the RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("original")
plt.show()


#average blur
dst1 = cv2.blur(img, ksize = (3,3))
plt.figure()
plt.imshow(dst1)
plt.axis("off")
plt.title("average blur")



#Gauss blur
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(dst1)
plt.axis("off")
plt.title("Gauss blur")



#Median blur
mb = cv2.medianBlur(img, ksize = 3)
plt.figure()
plt.imshow(dst1)
plt.axis("off")
plt.title("Median blur")













