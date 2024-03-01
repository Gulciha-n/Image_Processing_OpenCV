import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "openCV.png"
img = cv2.imread(path)
cv2.imshow("OpenCV",img)
print("shape :{}".format(img.shape))

(B , G , R) = cv2.split(img)

# merge images that splitted
merged = cv2.merge([B , G , R])

#create a black screen

black = np.zeros(img.shape[:2] , dtype="uint8")
#cv2.imshow("Black_screen",black)
'''
dtype=np.uint8 represents an 8-bit (1-byte) integer
data type and is typically used to store values between 0 and 255.
'''

cv2.imshow("Blu",cv2.merge([B, black ,black]))
cv2.imshow("Green",cv2.merge([black ,G ,black]))
cv2.imshow("Red", cv2.merge([black,black,R]))

cv2.waitKey(0) 
cv2.destroyAllWindows()


