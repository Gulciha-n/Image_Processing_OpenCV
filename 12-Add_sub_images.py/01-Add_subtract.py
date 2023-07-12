import cv2 

img1 = cv2.imread("space1")

img2 = cv2.imread("space2")

cv2.imshow("1", img1)
cv2.imshow("2", img2)

#addition
add_imgs = cv2.add(img1, img2)
cv2.imshow("addition",add_imgs)

#addition according to weights
#alpha + beta = 1
result1 = cv2.addWeighted(src1=img1, alpha=0.2, src2=img2, beta=0.8, gamma=0)
cv2.imshow("as_weight", result1)




#subtraction
img3 = cv2.imread("grey1.jpg")
img4 = cv2.imread("grey2.jpg")

cv2.imshow("grey1", img3)
cv2.imshow("grey2", img4)

result2 = cv2.subtract(img3,img4)
cv2.imshow("result2", result2)



cv2.waitKey(0)
cv2.destroyAllWindows()


