import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur = cv2.blur(img_filter,(9,11)) #genişlikte 9 piksel, yükseklikte 11 piksellik bir bulaniklaştirma 
blur2 = cv2.GaussianBlur(img_filter,(7,7),cv2.BORDER_DEFAULT) #tek sayilar kullanilir çünkü bu, filtre merkezinin bir pikselin tam merkezine gelmesini sağlar

blur_m = cv2.medianBlur(img_median,5)

blur_b = cv2.bilateralFilter(img_bilateral, 9,95,95)

# cv2.imshow("img_filter",img_filter)
# cv2.imshow("blur_filter",blur)
# cv2.imshow("blur_filter2",blur2)
# cv2.imshow("img_median",img_median)
# cv2.imshow("blur_median",blur_m)
cv2.imshow("Original_bilateral",img_bilateral)
cv2.imshow("bilateral",blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()