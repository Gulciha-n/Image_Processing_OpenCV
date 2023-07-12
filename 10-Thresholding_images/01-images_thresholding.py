import cv2
import matplotlib.pyplot as plt

#3import image
img = cv2.imread("img1.JPG")

#convert color to gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img,cmap="gray")
#close axis
plt.axis("off")
plt.show()


#thresholding
_,thres_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thres_img,cmap="gray")
plt.axis("off")
plt.show()


_,thres_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)

plt.figure()
plt.imshow(thres_img,cmap="gray")
plt.axis("off")
plt.show()


#adaptive thresholding
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

plt.figure()
plt.imshow(thresh_img2,cmap = "gray")
plt.axis("off")
plt.show()


''' 
- `255`: Maximum pixel value. If a pixel value exceeds the threshold value, it is assigned this value.
- `cv2.ADAPTIVE_THRESH_MEAN_C`: Uses the mean value as the adaptive thresholding method. 
- `cv2.THRESH_BINARY`: The thresholding type used to determine the values of thresholded pixels.
 Here, if a pixel value exceeds the threshold, it is assigned white, otherwise black.
- `11`: Window size. Specifies the window size used for each region during the adaptive thresholding 
process. In this case, an 11x11 window size is used.
- `8`: Remaining term for desired threshold value calculation. Specifies the coefficient used during the 
calculation of the mean or weighted mean. 

'''





