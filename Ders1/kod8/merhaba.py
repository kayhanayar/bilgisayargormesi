
import sys
import cv2

image = cv2.imread("deneme.png")

height,width,channels = image.shape 
##resim büyütmek için kübik  veya lineer enterpolasyon (ara değer bulma) 
## tekniği kullanmak daha iyi sonuçlar verecektir.
## Kübik enterpolasyon daha fazla işlem gücü gerektirmektedir
buyukResim = cv2.resize(image,(width*2,height*2),interpolation=cv2.INTER_LINEAR)


cv2.imshow("olcekli",buyukResim)
cv2.waitKey(0)
cv2.destroyAllWindows()
##küçültme yaparken alan enterpolasyon kullanılmaktadır.
#piksel değerleri bulundukları alana göre yeni değerlerini almaktadır.
kucukResim = cv2.resize(image,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

cv2.imshow("olcekli",kucukResim)
cv2.waitKey(0)
cv2.destroyAllWindows()