import argparse

parser = argparse.ArgumentParser()

parser.add_argument("ilk_arguman",help="ilk arguman yardım");

#ilk parametremiz otomatik olarak string türünde değer alacaktır.
#ikinci parametrenin tamsayı alabilmesi için fonksiyona yeni bir parametre ekliyoruz
#bu parametre içerisinde type değerini kullanıyoruz
parser.add_argument("ikinci_arguman",help="ikinci arguman yardım",type=int);

parser.add_argument("ucuncu_arguman",help="ucuncu arguman yardım",type=int);

args = parser.parse_args()

print(args.ilk_arguman)
print(args.ikinci_arguman)
print(args.ucuncu_arguman)