import cv2

cap = cv2.VideoCapture("body.mp4")

body_cascade = cv2.CascadeClassifier("D:\\Codes_VSCode\\OpenCV_Files\Haar_Cascade\\fullbody.xml")

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("video",frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release

cv2.destroyAllWindows()


