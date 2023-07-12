import cv2

img = cv2.imread("image.png")
cv2.imshow("orijinal", img)

B,G,R = cv2.split(img)

cv2.imshow("Blue", B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)


#merge images
merge = cv2.merge((B,G,R))
cv2.imshow("merge", merge)


cv2.waitKey(0)
cv2.destroyAllWindows()
