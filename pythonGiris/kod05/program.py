import sys
#döngüler
#sayaç ile for döngüsü yapabilmek için range fonksiyonu kullanılabilir
#aşağıdaki döngü 5 defa döner. x 0 dan başlayarak değeri birer artar

for x in range(0,5):
    print(x)
print("--------------------------")

#aynı işlemi aşağıdaki döngü ile de gerçekleştirilebilir.
for x in range(5):
    print(x)
print("--------------------------")

#eğer artışın miktarını değiştirmek istiyorsanız aşağıdaki gibi döngü yazabilirsiniz.
for x in range(2,10,3):
    print(x)

#iç içe döngüler
for x in range(0,5):
    for y in range(0,5):
        print(str(x)+" "+str(y))

