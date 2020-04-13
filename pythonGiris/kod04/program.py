import sys

#koşul için if anahtar kelimesi kullanılır
# if kelimesinden sonra koşul belirtililir
# koşula bağlı komutlar yazılmadan önce : operatörü yazılması gerekir.
# operatörler
# == , >= ,<= , != ,>, <,
sayi1=5
sayi2= 10

if sayi2>sayi1:
    print("sayi2 sayi1 den büyüktür.")

#elif c++ dilindeki elseif'e benzemektedir. 
#koşulun aralığını daraltmak için kullanılmaktadır.

sayi1 = 20
sayi2 = 15

if sayi2>sayi1:
    print(" sayi2 sayi1 den büyüktür")
elif sayi1>sayi2:
    print("sayi1 sayi2 den büyüktür")

#yukarıda dikkat etmeniz gereken python dilinde komut blokları her satırın konumu ile ilişkilidir
#koşula ait komutları bir tab boşluk bırakarak yazmamız gerekir.
#aşağıdaki örnekde if koşuluna ait olan 2 satır bulunrmaktadır. üçüncü satır koşula ait değildir.


if sayi2<sayi1:
    print(" birinci satır")
    print(" ikinci satır")
print("bu satır koşula ait değildir.")

#aşağıdaki kod bloğunda da grammer hatası yapılmıştır.
#ikinci print satırı 2 defa boşluk bırakıldığı için
#if bloğuna ait değildir.
#if bloğunun ait olduğu bloğa aittir( anlaması biraz zor evet)
#fakat if bloğu kimseye ait olmadığı için derleyici 2.print satırını hatalı göstermektedir.

#if sayi2<sayi1:
#    print(" birinci satır")
#        print(" ikinci satır")
#    

#else ifadesinin kullanımı da aşağıdaki gibidir

if sayi2==sayi1:
    print("sayilar eşittir")
else:
    print("sayilar eşit değildir.")

#çoklu koşul ve işlemi

if sayi1!=sayi2 and sayi2>sayi1:
    print("iki koşulunda doğru olma durumu")

if sayi1!=sayi2 or sayi2>sayi1:
    print("iki koşuldan birinin doğru olma durumu")

