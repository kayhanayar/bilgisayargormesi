import sys
import cv2

#Resimi siyah-beyaz olarak yükleme (GRayscale)
#bu formatta tek bir renk ve tonları bulunmaktadır.
resim = cv2.imread("deneme.png",cv2.IMREAD_GRAYSCALE)

#boyut sadece genislik ve yükseklik bilgilerini tutacaktır.
#siyah beyaz resimlerde kanal bilgisi bulunmaz.
boyut = resim.shape;

print("boyut:"+str(boyut))

#piksel bilgisi sadece beyaz renginin tonlarını tutmaktadır.
# o yüzden aşağıdaki işlem sonucun da tek bir değer dönecektir 
#o değeri de i değişkeni içerisinde tuttuk
i = resim[6,40];

print("beyaz yoğunluğu:"+str(i));

cv2.imshow("Merhaba",resim)

cv2.waitKey(0);