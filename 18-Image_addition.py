import cv2
import numpy as np

image = np.zeros((500,500,3) ,np.uint8) + 255
circle = cv2.circle(image,(200,200), 50 , (255,0,0) , -1)

image2 = np.zeros((500,500,3) ,np.uint8) + 255
rectangle = cv2.rectangle(image2,(150,150) , (300,300) ,(0,255,0), -1)

adding = cv2.add(circle,rectangle)
print(adding)

cv2.imshow("circle",image)
cv2.imshow("rectangle",image2)
cv2.imshow("add",adding)

cv2.waitKey(0)
cv2.destroyAllWindows()
