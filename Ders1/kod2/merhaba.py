import sys
import cv2

resim = cv2.imread("deneme.png")

#resimdeki piksel bilgilerine bir dizi elemanına eriştiğimiz
#gibi erişebilmekteyiz. aşağıda 40 sütun 6. satır pikselinin 
#renkg değeri getirilmektedir. PNG formatında piksel renk 
#değerleri BGR (blue,green,red) şeklinde saklandığı için
#diziden alaınan elemanın da 3 farklı değişkene yerleştirilmesi gerekmektedir.
#python üç değer döndürmeye imkan tanımaktadır.

b,g,r = resim[6,40]

print(b,g,r)
#aynı şekilde bir piksele yeni değer atamak istediğimizde renk 
#değerlerini ayrı ayrı vermeyliyiz

resim[6,40]=0,0,255

#bazen resimden bir piksel yerine bir bölge almak isteyebiliriz
#bunun içinde aşağıdaki gibi istediğimiz bölgeyi belirtmemiz gerekir.

sol_ust_kose = resim[0:100,0:100]

cv2.imshow("Merhaba",sol_ust_kose)

cv2.waitKey(0);