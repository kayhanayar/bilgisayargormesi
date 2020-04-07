import sys
import cv2
import numpy as np
image = cv2.imread("doomslayer.png")

height,witdh,channel = image.shape
cv2.imshow("pencere1",image)

box_kernel = [[1, 1 , 1 ],
              [1, 1 , 1 ],
              [1, 1 , 1 ]]
              
for y in range(0,height):
    for x in range(0,witdh):
       
        toplam = [0,0,0]
        kxmax = 1
        kymax = 1
        kymin = -1
        kxmin = -1

        if (x+1)>=witdh:
            kxmax = 0
        if (y+1)>=height:
            kymax = 0
        if (x-1)<0:
            kxmin = 0
        if (y-1)<0:
            kymin = 0

        for ky in range(kymin,kymax+1):
            for kx in range(kxmin,kxmax+1):
               
                lastX = x+kx
                lastY = y+ky
                toplam[0] = toplam[0]+image[lastY,lastX][0]
                toplam[1] = toplam[1]+image[lastY,lastX][1]
                toplam[2] = toplam[2]+image[lastY,lastX][2]

        toplam[0] = toplam[0]/9
        toplam[1] = toplam[1]/9
        toplam[2] = toplam[2]/9

        image[y,x] = toplam
        #print("---------------------")


cv2.imshow("pencere2",image)
cv2.waitKey(0)
cv2.destroyAllWindows()