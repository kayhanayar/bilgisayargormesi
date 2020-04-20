#kalıtım
class Sekil:
    def __init__(this):
        this.x = 10
        this.y = 5
        print("Sekil oluşturuldu")
    def koordinatYaz(this):
        print("x,y:"+str(this.x)+","+str(this.y))

#dikdortgen Sekil sınıfından kalıtım alıyor
class Dikdortgen(Sekil):
    def __init__(this,genislik,yukseklik):
        this.genislik = genislik
        this.yukseklik =yukseklik
        print("Dikdortgen oluşturuldu")
#Kalıtım alınırken temel sınıfın kurucusu çağrılmamaktadır.
d1 = Dikdortgen(100,200)

class Daire(Sekil):
    def __init__(this,yaricap):
        ##temel sınıfın kurucusu çağrılıyor
        Sekil.__init__(this)
        this.yaricap = yaricap
        print("Daire olusturuldu")

c1 = Daire(100)
print(c1.x)
#temel sınıfın metotu da çocuk nesne tarafından çağrılabilir.
c1.koordinatYaz()

