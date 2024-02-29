import cv2
img = cv2.imread("image_read.py\image_read\clone.jpg",0)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#resize
#img = cv2.resize(img , (620,480))
cv2.imshow("image",img)
#save image
cv2.imwrite("clone1.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


