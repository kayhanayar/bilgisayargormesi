from PyQt5.QtWidgets import *

app = QApplication([])
win = QMainWindow()
button = QPushButton('Test')
win.setCentralWidget(button)
win.show()
app.exit(app.exec_())