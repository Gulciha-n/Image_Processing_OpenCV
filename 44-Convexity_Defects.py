import cv2
import numpy as np

img = cv2.imread("star.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
_,thresh = cv2.threshold(blur,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)
cnt = contours[0]
print(cnt)
hull = cv2.convexHull(cnt,returnPoints=False) # contour'un dış sınırlarını veya şeklini ifade eden convex hull'u hesaplar
defects = cv2.convexityDefects(cnt,hull) #defects dizisi kontur noktalarının indekslerini içerir.

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0]) #birinci  s indeksine sahip noktasının x koordinatını
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,0,255],3)
    cv2.circle(img,far,4,[0,255,0],-1)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

