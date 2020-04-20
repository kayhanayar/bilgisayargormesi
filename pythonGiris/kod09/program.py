#sınıf tanımlama
#class anahtar kelimesi ile sınıf ismi kullanılır
class Dortgen:
    #__init__ fonksiyonu kurucu fonksiyon görevi yapmaktadır
    #python da bütün methodların ilk parametresi self değeridir
    #self oluşturulacak nesneyi gösteren bir referanstır.
    #isim self olmak zorunda değildir. bu parametre derleyici tarafından girilecektir
    #yani isim sizin kullanımınız için gereklidir.
    #hangi ismi verdiyseniz metot içerisinde nesneye erişmek için o ismi kullanmak zorundasınız.

    def __init__(self,genislik,yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
        
    def alanYazdir(baskaIsim):
        #self yerine baskaIsim kullandık.
        #isim dışında değişen birşey yok.
        #sınıf elemanlarına erişirken referansı kullanmak zorundayız.
        alan = baskaIsim.genislik*baskaIsim.yukseklik
        print("Sınıf Alanı:"+str(alan))


d1 = Dortgen(100,200)

print(d1.genislik)
print(d1.yukseklik)

d1.alanYazdir()