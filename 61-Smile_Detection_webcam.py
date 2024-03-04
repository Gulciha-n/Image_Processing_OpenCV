import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("D:\\Codes_VSCode\\OpenCV_Files\\Haar_Cascade\\Frontal_Face.xml")
smile_cascade = cv2.CascadeClassifier("D:\\Codes_VSCode\\OpenCV_Files\Haar_Cascade\\smile.xml")

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.2,2)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    roi_frame = frame[y:y+h,x:x+h]
    roi_gray = gray[y:y+h,x:x+h]

    smiles = smile_cascade.detectMultiScale(roi_gray,1.5,2)
    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_frame,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

    cv2.imshow("smiles",frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break