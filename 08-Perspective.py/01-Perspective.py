import cv2
import numpy as np

#import image
img = cv2.imread("image.png")
cv2.imshow("original", img)

width = 400
height = 500

#generate a matris with pixel values of corners

pts1 = np.float32([[230,1],[1,142],[540,150],[338,617]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
 
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

img_output=cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("convertedimg", img_output)
