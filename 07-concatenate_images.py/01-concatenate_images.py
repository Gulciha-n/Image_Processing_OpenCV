import cv2
import numpy as np

img = cv2.imread("images.png")

cv2.imshow("orijinal", img)

#concatenate vertical
vertical_img = np.vstack((img,img))
cv2.imshow("Vertical_img", vertical_img)


#concatenate horizontal
horizontal_img = np.hstack((img,img))
cv2.imshow("horizontal_cont", horizontal_img)

