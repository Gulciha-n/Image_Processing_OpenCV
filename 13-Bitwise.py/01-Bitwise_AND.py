import cv2

img1 = cv2.imread("bit1.png")
img2 = cv2.imread("bit2.png")


and_ = cv2.bitwise_and(img1, img2)
cv2.imshow("and", and_)


cv2.imshow("bit1", img1)
cv2.imshow("bit2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# white = 1, black = 0
# 1 & 1 = 1 , 1 & 0 = 0

