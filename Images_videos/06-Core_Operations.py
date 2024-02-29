import cv2
import numpy as np

path = "sunset.jpg"
img = cv2.imread(path)
#print(img)

px = img[10,10]
print(px)

#BGR
(b,g,r) = img[15,15]
print("[15,15] - Blue :{} , Green :{} , Red :{}".format(b,g,r))

print("--------------------------")

print(img[10,10])
print(img[10,10,0])

print("--------------------------")
#BGR -accessing values of pixel
blue = img[15,15,0]
green = img[15,15,1]
red = img[15,15,2]

print(blue , green , red)

print("--------------------------")

print("before :",img[15,15])
img[15,15] = [255,255,255]
print("after :",img[15,15])

#accessing values of pixel - 2 - BGR
print("Red value :",img.item(10,10,2))


img[10,10] = [255,255,100]
print(img[10,10])
#or
img.itemset((10,10,2),100)
print(img[10,10])


