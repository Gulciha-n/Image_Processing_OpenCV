import cv2

cap = cv2.VideoCapture(0)

while True:
    
    #take an image and assignment to the "frame"
    # _ = open the camera or not
    _,frame = cap.read()
    #0xff == ord("q") => key pressed is "q" ?
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
