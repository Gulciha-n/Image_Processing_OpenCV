import cv2

img = cv2.imread("D:\\OpenCV_Files\\Test_Images\\face.png")

face_cascade = cv2.CascadeClassifier("D:\\OpenCV_Files\\Haar_Cascade\\Eye_cascade.xml")
#Haar Cascade sınıflandırıcısının modelini depolar.

eye_cascade = cv2.CascadeClassifier("D:\\OpenCV_Files\\Haar_Cascade\\Eye_cascade.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.2,5)

for (x,y,h,w) in faces:
    cv2.rectangle(img,(x,y),(x+h,y+w),(0,0,255),2)

#tespit ettiğimiz yüzü bir değişkene atayıp bunun içinde göz algılayalım
img2 = img[y:y+h , x:x+w]
gray2 = gray[y:y+h , x:x+h]

#şimdi detectMultiScale ile belirlediğimiz bölgede gözler arayalım
eyes = eye_cascade.detectMultiScale(gray2)

for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2,(ex,ey),(ew,eh),(255,0,0),2)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()







