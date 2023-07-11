import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

cv2.imshow("black image", img)

#line
#BGR for green = (0,255,0)
#BGR gor red = (0,0,255)
#BGRfor blue = (255,0,0)
#(img , start point , end point ,color,thickness)
cv2.line(img,(0,0),(512,512),(0,255,0),5)
cv2.imshow("line",img)

#line
cv2.line(img,(512,0),(0,512),(255,0,0),5)
cv2.imshow("line",img)

#rectangle 
# ()
cv2.rectangle(img,(0,0) ,(256,256), (255,255,0))
cv2.imshow("rectangle",img )


#fill in the rectangle
cv2.rectangle(img,(50,50) ,(100,100), (255,255,0),cv2.FILLED)
cv2.imshow("rectangle",img )

#circle
cv2.circle(img,(300,300), 45 , (0,0,255))
cv2.imshow("circle", img)


#fill in the circle 
cv2.circle(img,(200,200), 45 , (0,0,255),cv2.FILLED)
cv2.imshow("circle", img)

#text
#parameters = (img, text, org, fontFace, fontScale, color)
cv2.putText(img,"hello", (355,355),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("text", img)












