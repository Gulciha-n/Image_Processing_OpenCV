import cv2

cap = cv2.VideoCapture("car.mp4")

car_cascade = cv2.CascadeClassifier("D:\\Codes_VSCode\OpenCV_Files\\Haar_Cascade\\car.xml")

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    #frame = cv2.resize(gray,(480,360)) #küçültünce iyi çalışmıyor
    cars = car_cascade.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("video",frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()


