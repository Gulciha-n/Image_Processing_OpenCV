import cv2
import numpy as np

def nothing():
    pass
img = np.zeros((512,512,3) , dtype=np.uint8)

cv2.namedWindow("frame")

cv2.createTrackbar("R" , "frame" , 0,255 , nothing)
cv2.createTrackbar("G" , "frame" , 0,255 , nothing)
cv2.createTrackbar("B" , "frame" , 0,255 , nothing)
cv2.createTrackbar("ONN/OFF" , "frame" , 0,1 , nothing)

while True:
    cv2.imshow("frame" , img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    r = cv2.getTrackbarPos("R" ,"frame")
    g = cv2.getTrackbarPos("G" ,"frame")
    b = cv2.getTrackbarPos("B" ,"frame")
    switch = cv2.getTrackbarPos("ONN/OFF" , "frame")

    if switch:
        img[:] = [r,g,b]
    else:
        img[:] = [0,0,0]
        
cv2.destroyAllWindows()


