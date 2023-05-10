import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "D:/computer vision/1.jpg"
img =  cv2.imread(path)
imgCanny = cv2.Canny(img,100,200)
cv2.imshow("Img Canny",imgCanny)
