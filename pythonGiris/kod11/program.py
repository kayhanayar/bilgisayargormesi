#kalıtım super anahtar kelimesi
class Sekil:
    def __init__(this):
        this.x = 10
        this.y = 5
        print("Sekil oluşturuldu")
    def koordinatYaz(this):
        print("x,y:"+str(this.x)+","+str(this.y))

#temel sınıfın ismi direk kullanmak kodumuzun değiştirilebilirliğini azaltıyor
#o yüzden super anahtar kelimesini kullanmak daha pratik.
class Dikdortgen(Sekil):
    def __init__(this,genislik,yukseklik):
        ##temel sınıfın kurucusu çağrılıyor
        #init parametre almaz.kim için çağrıldığı belli.
        super().__init__()
        this.genislik = genislik
        this.yukseklik =yukseklik
        print("Dikdortgen oluşturuldu")
    def yaz(this):
        #temel sınıfın fonksiyonu çağrılıyor
        super().koordinatYaz()
        print("genislik,yukseklik:"+str(this.genislik)+","+str(this.yukseklik))
#Kalıtım alınırken temel sınıfın kurucusu çağrılmamaktadır.
d1 = Dikdortgen(100,200)
d1.yaz()
class Daire(Sekil):
    def __init__(this,yaricap):
        ##temel sınıfın kurucusu çağrılıyor
        super().__init__()
        this.yaricap = yaricap
        print("Daire olusturuldu")


c1 = Daire(100)
print(c1.x)
#temel sınıfın metotu da çocuk nesne tarafından çağrılabilir.
c1.koordinatYaz()

