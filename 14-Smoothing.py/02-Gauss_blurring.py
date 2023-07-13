import cv2
import numpy as np
import matplotlib.pyplot as plt



def gaussianNoise(image):
    row , col , ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean , sigma ,(row,col,ch))
    noisy = image + gauss
    
    return noisy


#import and normalize 
#normalize = 0-255 => 0-1
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)/255

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orjinal")
plt.show()

#gaussian noise
gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Image with Gaussian Noise")
plt.show()



#gaussian blurring
gb = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Image with Gaussian Blurring")

















