import argparse
import sys
import cv2

image = cv2.imread("deneme.png")

b,g,r = cv2.split(image)

new_image = cv2.merge((g,r,b))

cv2.imshow("ilk resim",image)

cv2.imshow("renk kanalları değiştirilmiş",new_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

#split fonksiyonu oldukça çok işlem yapmaktadır
#onun yerine Numpy kütüphanesinin sağladığı bir aracı kullanacağız
#aşağıda image dizisinin 0. kanalını yani mavi kanalını ayıracağız.
#şuan b sadece bir kanalı temsil ediyor.
b= image[:,:,0]
#eğer bu kanalı ekrana çıkartmak istersek siyag beyaz çıkar ve sadece mavi
#rengin olduğu yerler beyaz olacaktır.
cv2.imshow("sadece maviler",b)

cv2.waitKey(0)

cv2.destroyAllWindows()

#istenirse bir kanal komple sıfır yapılabilir
#bu seyede resimden ilgili kanal komple çıkartılmış olur
mavisizResim = image.copy()

mavisizResim[:,:,0]=0

cv2.imshow("sadece maviler",mavisizResim)
cv2.waitKey(0)