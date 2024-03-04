import cv2

cap = cv2.VideoCapture("car.mp4")

car_cascade = cv2.CascadeClassifier("D:\\Codes_VSCode\\OpenCV_Files\\Haar_Cascade\\car_cascade\\classifier\\cascade.xml")

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame , (640,480))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(frame,1.3,3)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("cars",frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

