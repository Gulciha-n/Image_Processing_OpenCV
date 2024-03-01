import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8) + 255

#line
cv2.line(canvas , (0,0) , (512,512) , (0,0,255) , thickness=4)
cv2.line(canvas, (0,100) , (100,0), (255,0,0) , thickness=3)

#rectangle
cv2.rectangle(canvas , (0,400), (400,0) , (255,0,0) ,thickness=3 )
cv2.rectangle(canvas , (20,20) , (50,50) , (0,0,255) , thickness=-1)

#circle
cv2.circle(canvas , (200,200) , (70) , (255,0,0) , thickness=3)
cv2.circle(canvas ,(300,300) , (20) , (0,255,0) , thickness=-1)

#triangle

p1 = (80,200)
p2 = (100,400)
p3 = (60,300)

cv2.line(canvas , p1,p2 , (0,0,0) , thickness=2)
cv2.line(canvas , p2,p3 , (0,0,0) , thickness=2)
cv2.line(canvas , p1,p3 , (0,0,0) , thickness=2)


#polyline fonction

points = np.array([[ [100,500] , [500,100] , [200,300] , [10,400] ]], np.int32)
cv2.polylines(canvas , points , True , (0,0,200) , thickness=3)

#ellipse 

cv2.ellipse(canvas , (200,200) , (50,20) ,10,  0,360  , (0,255,0) , thickness=3)
cv2.ellipse(canvas , (400,400) , (80,30) ,10,  90,360  , (0,0,255) , thickness=-1)

cv2.imshow("Image",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

