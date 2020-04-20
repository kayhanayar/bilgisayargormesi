import sys
import cv2
import numpy as np

image = cv2.imread("deneme.png")

height,witdh,channels = image.shape

M = cv2.getRotationMatrix2D((witdh/2,height/2),90,1)

dst = cv2.warpAffine(image,M,(witdh,height))

cv2.imshow("ilk hal",image)

cv2.imshow("döndürülmüş",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()