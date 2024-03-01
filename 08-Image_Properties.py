import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "openCV.png"
img = cv2.imread(path)
cv2.imshow("openCV",img)

#dimension of image = height , width , channel
# channel :3  => color
# channel :1  => grayscale
print(img.shape)

print("Height : {} pixels".format(img.shape[0]))
print("Width :{} pixels".format(img.shape[1]))
print("channel :{} pixels".format(img.shape[2]))

'''
if image in grayscale, image don't have the channel because there isn't the second index
if image in color mode, we can write => img.shape[2]
'''

print("Image size : {}".format(img.size))
# image size = 211*239*3  (height*width*channel) 
# image size for grayscale image = 211*239*1

print("Data type : {}".format(img.dtype))
#data type unsigned integer 8-bit

cv2.waitKey(0)
cv2.destroyAllWindows()

