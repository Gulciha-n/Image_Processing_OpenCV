import cv2
import numpy as np

cap = cv2.VideoCapture("line.mp4")

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(640,480)) #görüntüye resize işlemi 
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #hsv,renkleri daha iyi tanımlamak ve ayırt etmek için
    lower_yellow = np.array([18,94,140],np.uint8)  #lower ve upper renk değerleri
    upper_yellow = np.array([48,255,255],np.uint8)

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow) #sarı renge ait pikselleri izole eden
    #hsv görüntüsü içerisindeki belirli bir renk aralığına ait pikselleri izole eder ve bunları beyaz bir maske üzerinde gösterir.
    edges = cv2.Canny(mask,75,250) #kenarlıkları çizdirelim.

    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(frame, (x1,y1),(x2,y2), (255,0,0),2)

    cv2.imshow("lines",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("edges",edges)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cv2.release()
cv2.destroyAllWindows()


