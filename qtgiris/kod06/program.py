from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui,QtCore


from Pencere import AnaPencere #Pencere dosyasını ekliyoruz
#AnaPencere için kendi sınıfımızı tasarlıyoruz.


app = QApplication([])
win = AnaPencere()
app.exit(app.exec_())