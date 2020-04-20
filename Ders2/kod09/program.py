from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui,QtCore


from Pencere import AnaPencere 
#AnaPencere için kendi sınıfımızı tasarlıyoruz.


app = QApplication([])
win = AnaPencere()
app.exit(app.exec_())