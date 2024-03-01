import cv2

cap = cv2.VideoCapture(0)

file_name = "D:\OpenCV -Udemy\webcam.avi"
codec = cv2.VideoWriter_fourcc("W","M","V","2")
frame_rate = 30 
resolution = (640,480)
VideoFileOutput = cv2.VideoWriter(file_name , codec , frame_rate ,resolution )
# Codec = coder-decoder 
while True:
    ret , frame = cap.read()
    if ret == 0 :
        break
    frame = cv2.flip(frame,1)
    VideoFileOutput.write(frame)
    cv2.imshow("webcam live",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

VideoFileOutput.release()
cap.release()
cv2.destroyAllWindows()


