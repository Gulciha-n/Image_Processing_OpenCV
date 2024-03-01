import cv2

cap = cv2.VideoCapture("Forest.mp4")

while True:
    ret , frame = cap.read() #videodan frame geldiği sürece frame'leri return et
    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    if ret == False:   # ret=return => video süresince frame'leri okur,bittiğinde yani bir okunacak bir frame kalmaduğında dööngüden çık.
        break
    cv2.imshow("video",frame)
    if cv2.waitKey(20) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()


