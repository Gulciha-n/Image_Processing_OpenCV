import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("D:\\OpenCV_Files\\Haar_Cascade\\Frontal_Face.xml")
eye_cascade = cv2.CascadeClassifier("D:\\OpenCV_Files\\Haar_Cascade\\eye_cascade2.xml")

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(480,360))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    roi_frame = frame[y:y+h , x:x+w]
    roi_gray = gray[y:y+h , x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    cv2.imshow("video",frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

