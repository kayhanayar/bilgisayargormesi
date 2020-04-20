from PyQt5.QtWidgets import *


from Pencere import AnaPencere #Pencere dosyasını ekliyoruz
#AnaPencere için kendi sınıfımızı tasarlıyoruz.


app = QApplication([])
win = AnaPencere()
app.exit(app.exec_())