import cv2 
import time

#video name
video_name = "MOT17-04-DPM.mp4"

#imort video
cap = cv2.VideoCapture(video_name)

#video dimension
print("width :",cap.get(3))
print("Height :",cap.get(4))


if cap.isOpened() == False:
    print("error")

#read video
while True:
    
    ret , frame = cap.read()

    if ret == True:
        time.sleep(0.01)
        cv2.imshow("video", frame)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()  #stop read
cv2.destroyAllWindows() 


















   

