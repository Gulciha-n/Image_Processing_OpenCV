import cv2
import numpy as np

canvas = np.zeros((600,600,3) , dtype=np.uint8) +255 

font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(canvas , "OpenCV" , (20,200) ,font1 ,4,  (0,255,0) , cv2.LINE_AA)
cv2.putText(canvas , "OpenCV" , (20,500) ,font3 ,5,  (0,255,0) , cv2.LINE_AA)

cv2.imshow("image" , canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


