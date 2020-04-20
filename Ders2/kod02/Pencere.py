from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QVBoxLayout,QHBoxLayout, QWidget,QLabel
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
import cv2
#AnaPencere için kendi sınıfımızı tasarlıyoruz.
class AnaPencere(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setGeometry(0,0,800,600)
        
        self.central_widget = QWidget()
        
        self.lblResim = QLabel("resim label",self.central_widget)
        self.lblResim2 = QLabel("resim label2",self.central_widget)
        self.btnResimYukle = QPushButton('Resim Yükle')

        self.btnFiltreUygula = QPushButton('Test')
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.hLayout = QHBoxLayout()

       

        
        self.layout.addWidget(self.btnResimYukle)
        self.layout.addWidget(self.btnFiltreUygula)
        self.layout.addLayout(self.hLayout)
        self.hLayout.addWidget(self.lblResim)   
        self.hLayout.addWidget(self.lblResim2)  
        self.setCentralWidget(self.central_widget)

        self.btnResimYukle.clicked.connect(self.resimYukle_pressed)

        self.btnFiltreUygula.clicked.connect(self.filtreUygula)

        self.show()
    def resimYukle_pressed(self):
        fileName = QFileDialog.getOpenFileName(self,"Open Image", "./", "Image Files (*.png *.jpg *.bmp)")
        self.image = cv2.imread(fileName[0])
        height, width, channel = self.image.shape

        bytesPerLine = 3 * width

        imageshow = cv2.cvtColor(self.image,cv2.COLOR_RGB2BGR)

        qImg = QtGui.QImage(imageshow.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)

        self.lblResim.setPixmap(QtGui.QPixmap.fromImage(qImg))

    def filtreUygula(self):
        
        self.blur_image = cv2.GaussianBlur( self.image, (7,7), 0)

        self.blur_image = cv2.cvtColor(self.blur_image,cv2.COLOR_RGB2BGR)
        height, width, channel = self.blur_image.shape

        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.blur_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)

        self.lblResim2.setPixmap(QtGui.QPixmap.fromImage(qImg))


