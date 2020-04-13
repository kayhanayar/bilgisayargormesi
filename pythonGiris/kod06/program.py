import sys
#diziler

# python da diziler köşeli parantezler ile tanımlanır

sayilar = [1,2,3,4,5,6]
print("sayilar = "+str(sayilar))

#dizinin ikinci elemanına erişmek için index kullanmak yeterlidiri

print("sayilar[2] = "+str(sayilar[2]))

#bir dizinin elemanlarını kullanarak yeni bir dizi oluşturabilirsiniz
#örneğin aşağıda sayilar dizinin 2. elamanından 5. elemanına kadar olan sayılar
#kullanılarak yeni bir dizi elde edilmiştiri
yeniSayilar = sayilar[2:5]

print("sayilar[2:5] = "+str(sayilar[2:5]))


#eğer index önüne : operatörü konursa verilen indeksten
#başlayıp dizinin başına doğru elemanlar alınır
#aşağıda 3. elemandan başlayıp dizinin başına kadar elemanlar alınır.
print("sayilar[:3] = "+str(sayilar[:3]))

#eğer indexden sonra : operatörü konursa indeksten başlayıp
#dizinin sonuna doğru sayılar getirilmektedir
#aşağıda 2. indeksten başlayıp dizinin sonuna kadar sayılar getirilir.
print("sayilar[2:] = "+str(sayilar[2:]))

#liste içerisinde döngü ile gezinme
print("----------- for siradaki in sayilar -----------")
for siradaki in sayilar:
    print(siradaki)
print("----------- for i in range(0,len(sayilar)) -----------")
for i in range(0,len(sayilar)):
    print(i)

#del komutu ile liste elemanlarını silebiliriz

del sayilar[3]

#veya komple diziyi silebiliriz

del sayilar

#istersek diziyi clear fonksiyonu ile boşaltabiliriz
sayilar.clear()

#eleman eklemek için append fonksiyonu kullanılabilir
#aşağıdaki satır sayilar dizisine 10 değerini eklemektedir.
sayilar.append(10);
