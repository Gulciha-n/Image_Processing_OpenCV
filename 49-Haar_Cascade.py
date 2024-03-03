#Haar yöntemi resim veya videolardaki hedeflenen nesnelerin algılanmasında kullanılır. 
#bunlar resim üzerindeki siyah ve beyazlıklardır.
#cascade = ard arda sıralı , kademeli

import cv2
img = cv2.imread("D:\\OpenCV_Files\\Test_Images\\face.png")

face_cascade = cv2.CascadeClassifier("D:\\OpenCV_Files\\Haar_Cascade\\Frontal_Face.xml")#Haar Cascade sınıflandırıcısının modelini depolar.
#CascadeClassifier:nesneleri (örneğin yüzleri) tanımak için eğitilmiş özellik sınıflandırıcıları içerir.
#Bu sınıf, verilen XML dosyasını yükler ve yüz tespiti yapmak için kullanılmak üzere hazır hale getirir.
#"xml" dosyaları nesnelerin (örneğin yüzler, gözler, arabalar vb.) tespit edilmesi için kullanılan Haar Cascade sınıflandırıcılarının özelliklerini ve eğitim verilerini içerir. 

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,4)  # 4 = hata ölçeklendirme hassaslık değeri
#resim üzerindeki yüzlerin koordinatları face_cascade içerisindeki koordinatlardan detectMultiScale ile yüzleri bulup faces içerisinde tutuyoruz.

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#(x,y) = sol üsk köşe koordinatları
#(x+w,y+h) = sağ alt koordinatları 

cv2.imshow("face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()





