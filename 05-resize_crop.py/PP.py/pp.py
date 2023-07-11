import cv2 

img = cv2.imread("pp.jpg.jpg")
cv2.imshow("orijinal", img)
print("dimension :", img.shape)

img_resize = cv2.resize(img,(550, 500))
cv2.imshow("re_img", img_resize)

cv2.imwrite("resizeimage.jpg", img_resize)
cv2.imshow("resizeimage.jpg", img_resize)
cv2.destroyAllWindows()

    


