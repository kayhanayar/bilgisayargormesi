import sys
import cv2
import numpy as np
image = cv2.imread("doomslayer.png",0)

height,witdh = image.shape
cv2.imshow("pencere1",image)
for y in range(0,height):
    for x in range(0,witdh):
        if image[y, x] >= 100:
            image[y, x] = 255  
        else:
            image[y, x] = 0

cv2.imshow("pencere2",image)
cv2.waitKey(0)
cv2.destroyAllWindows()