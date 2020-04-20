from PyQt5.QtWidgets import *

def button1_pressed():
    print("Button1 Pressed")
def button2_pressed():
    print("Button2 Pressed")

app = QApplication([])
win = QMainWindow()
#merkez form elemanı oluşturuyoruz.
#butonlarımız bu eleman içerisinde tutulacak.
central_widget = QWidget()
#buttonlar oluşturulduğunda koordinatları 0,0 olduğundan
#ilk butonun koordinatını değiştiriyoruz.
button1 = QPushButton('Test', central_widget)
button1.setGeometry(0,50,120,40)
button2 = QPushButton('Second Test', central_widget)

button1.clicked.connect(button1_pressed)
button2.clicked.connect(button2_pressed)

win.setCentralWidget(central_widget)
win.show()
app.exit(app.exec_())