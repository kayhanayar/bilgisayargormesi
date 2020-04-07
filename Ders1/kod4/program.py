import sys
import cv2
#sys.argv dizisi içerisinde komut satırından gelen parametreleri barındırır.
#ilk parametre her programlama dilinde olduğu gibi çalıştırılan uygulamanın tam yoludur
print(sys.argv[0]);

#istersek ekrana biçimli çıktı alabiliriz. '{}' içerisine 
# format fonksiyonun ilk parametresi yerleştirilir
#eğer birden fazla '{}' olsaydı format fonksiyonun da buna
#göre parametre sayısının artması gerekirdi.

print("calistirilan program:'{}'".format(sys.argv[0]))

#dışarıdan girilen parametre sayısı len(sys.argv) ile elde edilebilir

print("parametre sayısı:'{}'".format(len(sys.argv)))

#dizinin hepsinin ekrana döklümü

print("parametreler:'{}'".format(str(sys.argv)))

cv2.waitKey(0);