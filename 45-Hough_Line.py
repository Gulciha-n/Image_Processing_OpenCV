import cv2
import numpy as np

img = cv2.imread("h_line.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,75,150)  #görselin kenarlıklarını çizdirelim

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)  #tespit edilen çizgileri line değişkeninde saklıyoruz[(x1, y1, x2, y2)]
print(lines) # => line'ların bulundukları yerleri dizi halinde yazdırır bunları çizdirmek için for döngüsü oluşturuyoruz.

for line in lines:
    x1,y1,x2,y2 = line[0]  #line'ların başlangıç(x1,y1) ve bitiş (x2,y2) noktaları 
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) 

'''
her çizgi kendi içinde bir dizi olarak saklanir. Yani, her bir çizgi bir dizi içinde 
tanimlanir ve bu dizi içinde x1, y1, x2, ve y2 değerleri bulunur.
'''

cv2.imshow("image",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges) 

cv2.waitKey(0)
cv2.destroyAllWindows()
