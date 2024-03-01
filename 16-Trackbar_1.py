import cv2
import numpy as np

def nothing():
    pass

canvas = np.zeros((300,400,3) , dtype=np.uint8) 
cv2.namedWindow("image")

cv2.createTrackbar("R","image", 0,255 , nothing)
cv2.createTrackbar("G","image", 0,255 , nothing)
cv2.createTrackbar("B","image", 0,255 , nothing)

while True:
    cv2.imshow("image",canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    r = cv2.getTrackbarPos("R" , "image")
    g = cv2.getTrackbarPos("G" , "image")
    b = cv2.getTrackbarPos("B" , "image")

    canvas[:] = [r,g,b]

cv2.destroyAllWindows()


