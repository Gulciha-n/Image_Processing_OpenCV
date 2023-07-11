import cv2

img = cv2.imread("images.png",0)

#visualize
cv2.imshow("First image", img)


keybrd = cv2.waitKey(0) %0xFF


if keybrd==27:
    cv2.destroyAllWindows()
elif keybrd == ord("a"):
    cv2.imwrite("cat_gray.jpg", img)


'''
cv2.waitKey(0) % 0xFF waits for the user to press a key. 
With the parameter 0, it waits for any key to be pressed. 

Esc key (27 ASCII value). If the Esc key is pressed, 
the cv2.destroyAllWindows() function is called to close all open windows.

(ord("a")). If the "a" key is pressed, the cv2.imwrite("cat_gray.jpg", img) 
function is called to save the img image as "cat_gray.jpg".
    
'''

