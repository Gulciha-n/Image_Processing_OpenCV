import cv2

cap = cv2.VideoCapture(0)

#width and height of the camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)


#start video recorder for windows
writer = cv2.VideoWriter("Video_recorder.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))

while True:
    
    ret , frame = cap.read()
    cv2.imshow("video",frame)
    
    #save
    writer.write(frame)  
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release() 
writer.release()
cv2.destroyAllWindows()


   
    