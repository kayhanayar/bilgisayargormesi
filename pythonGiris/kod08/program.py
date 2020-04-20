#fonksiyon tanımlama
#def anahtar kelimesi kullanılarak tanımlanır.
#def den sonra fonksiyon ismi gelir. 
def fonksiyonIsmi():
    print("Merhaba ilk fonksiyonu tanımladık")

#fonksiyonu çağırmak için adını kullanmak yeterli olacaktır

fonksiyonIsmi()

#fonksiyon parametreleri virgül ile ayrılır. sadece parametere isimleri yazılır.
def alanHesapla(genislik,yukseklik):
    print("Genislik:"+str(genislik))
    print("Yukseklik"+str(yukseklik))
    print("Alan:"+str(genislik*yukseklik))
#argümanlar parametre sırasına göre verilir.
alanHesapla(20,30)

#eğer istersek argüman isimleri kullanarakta değer atayabiliriz
#bu yolla argüman sırasına uymamaız da gerekmez.

alanHesapla(yukseklik=10,genislik=20)

#parametrelere varsayılan değer verebiliriz.
def isimYazdir(isim="varsayilanİsim"):
    print(isim)

isimYazdir("Ahmet")
#varsayılan değer kullanılacaktır.
isimYazdir()

#fonksiyonların dönüş tipini belirtmek zorunda değiliz
#return ile dönüş değerini çağırmamız fonksiyonun dönmesi için yeterli olacaktır.
def ustAl(taban,ust):
    sonuc=1
    for x in range(0,ust):
        sonuc*=taban
    return sonuc

#Tek yapmamız fonksiyonu çağırmak o bize dönüş değerini getirecektir.
print(ustAl(2,4))