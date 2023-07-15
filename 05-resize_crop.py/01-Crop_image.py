import cv2

img = cv2.imread("images.jpg")
# 0 = gray , none = orijinal
print("Dimension of image :",img.shape)
cv2.imshow("orijinal", img)

#resized
img_resize=cv2.resize(img,(700,500))
print("Resize image shape :",img_resize.shape)
cv2.imshow("img resized", img_resize)


#crop (height , width)
img_croped = img[:100,:200]
cv2.imshow("Croped image", img_croped)
