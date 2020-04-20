from PyQt5.QtWidgets import *

#form elemanlarınnın koordinatlarını ve boyutlarını istediğimiz gibi 
#verebiliriz fakat pencerenin boyutu değiştirildiğinde 
#form elemanları bu değişime adapte olaamazlar. İstersek adapte olmalarını
# layout kullanarak sağlayabiliriz.
app = QApplication([])
win = QMainWindow()
central_widget = QWidget()
button2 = QPushButton('Second Test', central_widget)
button = QPushButton('Test', central_widget)
layout = QVBoxLayout(central_widget)
layout.addWidget(button2)
layout.addWidget(button)
win.setCentralWidget(central_widget)
win.show()
app.exit(app.exec_())