import cv2
import dlib

detector = dlib.get_frontal_face_detector()


cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    faces = detector(frame)
    
    for face in faces:
        x= face.left()
        y= face.top()
        w= face.right()
        h= face.bottom()
        cv2.rectangle(frame, (x,y),(w,h),(0,0,255),2)
        
    
    cv2.imshow("farme", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
