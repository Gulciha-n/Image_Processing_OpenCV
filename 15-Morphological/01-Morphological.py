import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("datai_team.jpg",0)
plt.figure()
plt.imshow(img,cmap = "gray" )
plt.axis("off")
plt.title("Original image")


#erosion 
kernel = np.ones((5,5) , dtype=np.uint8)
result = cv2.erode(img , kernel ,iterations =1)
plt.figure()
plt.imshow(result,cmap = "gray" )
plt.axis("off")
plt.title("erosion image")


#dilation 

result2 = cv2.dilate(img, kernel)
plt.figure()
plt.imshow(result2,cmap = "gray" )
plt.axis("off")
plt.title("dilation image")


#white noise

WhiteNoise = np.random.randint(0,2 , size =img.shape)
WhiteNoise  =WhiteNoise*255
plt.figure()
plt.imshow(WhiteNoise, cmap = "gray")
plt.axis("off")
plt.title("White noise")

noise_img = WhiteNoise + img
plt.figure()
plt.imshow(noise_img, cmap = "gray")
plt.axis("off")
plt.title("noise_img")


#opening 

opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN ,kernel)
plt.figure()
plt.imshow(opening, cmap = "gray")
plt.axis("off")
plt.title("opening")


#black noise

balckNoise = np.random.randint(0,2 , size =img.shape)
balckNoise  =balckNoise*-255
plt.figure()
plt.imshow(balckNoise, cmap = "gray")
plt.axis("off")
plt.title("black Noise")

black_noise_img = balckNoise + img
black_noise_img[black_noise_img <= -255 ] = 0
plt.figure()
plt.imshow(black_noise_img, cmap = "gray")
plt.axis("off")
plt.title("black_noise_img")


#closing

closing = cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE ,kernel)
plt.figure()
plt.imshow(closing, cmap = "gray")
plt.axis("off")
plt.title("closing")




#morphology gradient

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient, cmap = "gray")
plt.axis("off")
plt.title("gradient")





































