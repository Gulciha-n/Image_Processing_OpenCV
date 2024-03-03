import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("D:\\OpenCV_Files\\Haar_Cascade\\Frontal_Face.xml")

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    faces = face_cascade.detectMultiScale(frame,1.3,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    
    cv2.imshow("img",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


