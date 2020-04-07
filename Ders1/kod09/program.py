import sys
import cv2
import numpy as np
image = cv2.imread("deneme.png")

height,witdh,channels = image.shape

M = np.float32([[1,0,300],[0,1,350]])

yeniResim = cv2.warpAffine(image,M,(cols,rows))
cv2.imshow("otelenmis",yeniResim)

cv2.waitKey(0)
cv2.destroyAllWindows()