import sys

#yazı işlemleri

yazi = "Merhabalar"

print(yazi)

#ilk karakteri getirmek için

print(yazi[0])

#yazıyı parçalamak için aşağıdaki format kullanılabilir
#3. karakterden 6. karaktere kadar olan kısmı ekrana çıkartacaktır.

print(yazi[3:6])

#yazının boyutunu getirmek için len fonksiyonu kullanılır

print(len(yazi))

#yazilari birleştirmek için + operatörü kullanılır

yazi  =yazi+ "Dünya"+yazi

print(yazi)