import cv2
import dlib

detector = dlib.get_frontal_face_detector()


cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    faces = detector(frame)
    print(faces)
    
    
    cv2.imshow("farme", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()


