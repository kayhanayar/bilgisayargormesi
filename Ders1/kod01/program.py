import sys
import cv2


image = cv2.imread("deneme.png")
#resim dosyasının boyutu genislikXyukseklikXKanal
#kanal bir pixel için kullanılan renk formatıdır. burada kaç bit 
print("dosya boyutu:"+str(image.size))

cv2.imshow("Merhaba",image)

cv2.waitKey(0);