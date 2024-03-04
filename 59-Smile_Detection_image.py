import cv2

img = cv2.imread("smilee.jpg")

face_cascade = cv2.CascadeClassifier("D:\\Codes_VSCode\\OpenCV_Files\\Haar_Cascade\\Frontal_Face.xml")
smile_cascade = cv2.CascadeClassifier("D:\\Codes_VSCode\\OpenCV_Files\Haar_Cascade\\smile.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,2)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

roi_img = img[y:y+h,x:x+h]
roi_gray = gray[y:y+h,x:x+h]

smiles = smile_cascade.detectMultiScale(roi_gray,1.3,5)
for (sx,sy,sw,sh) in smiles:
    cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(255,0,0),2)

cv2.imshow("faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

