import cv2
import numpy as np

#f(x,y) = x*a + y*b + c

image = np.zeros((500,500,3) ,np.uint8) + 255
circle = cv2.circle(image,(200,200), 50 , (255,0,0) , -1)

image2 = np.zeros((500,500,3) ,np.uint8) + 255
rectangle = cv2.rectangle(image2,(150,150) , (300,300) ,(0,0,255), -1)

add = cv2.addWeighted(circle , 0.7 ,rectangle , 0.3 , 0)

cv2.imshow("circle",image)
cv2.imshow("rectangle",image2)
cv2.imshow("add" , add)
cv2.waitKey(0)
cv2.destroyAllWindows()

