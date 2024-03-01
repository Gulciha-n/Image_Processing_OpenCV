import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "openCV.png"
img = cv2.imread(path)
cv2.imshow("OpenCV",img)
print("shape :{}".format(img.shape))

(B , G , R) = cv2.split(img)
cv2.imshow("OpenCV-B",B)
cv2.imshow("OpenCV-G",G)
cv2.imshow("OpenCV-R",R)

# merge images that splitted
merged = cv2.merge([B , G , R])
cv2.imshow("Merged",merged)


cv2.waitKey(0) 
cv2.destroyAllWindows()

