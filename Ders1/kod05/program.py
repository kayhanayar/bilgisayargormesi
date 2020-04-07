# Bu uygulamada argparse kütüphanesinin kullanımını gösteriyoruz
# programa gelen argümanları daha iyi kontrol etmek için kullanılıyor.

import argparse

#parser nesnesi oluşturuluyor
parser = argparse.ArgumentParser()

#parser nesnesine kullanıcıdan alınacak bir argüman tanıtılıyor
#ilk parametre argümanın alacağı değişken ismi 
#ikinci parametre argümanın yanında çıkacak olan yardım mesajı

parser.add_argument("ilk_arguman",help="ilk arguman yardım");

#argümanlar yakalanıyor
args = parser.parse_args()

#ilk argümanın değeri ekrana çıkartılıyor
print(args.ilk_arguman)