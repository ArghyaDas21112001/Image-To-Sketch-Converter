#image to sketch Program 
import cv2
import time
image = cv2.imread("smile.jpg")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21,21), 0)
invertblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertblur, scale=256.0)
cv2.imwrite("sketch.png",sketch)



#cv2.imshow("greyimage",grey_img)
#time.sleep(1000)
