
from PyQt5.QtWidgets import *

from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
import cv2

#AnaPencere için kendi sınıfımızı tasarlıyoruz.
class AnaPencere(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setGeometry(0,0,800,600)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerfunction)

        self.central_widget = QWidget()
        
        self.lblResim = QLabel("resim label",self.central_widget)
        #ImageView nesnesi oluşturuluyor
        self.lblResim2 = QLabel("resim label2",self.central_widget)

        self.btnResimYukle = QPushButton('KameraBaşlat')
        self.btnFiltreUygula = QPushButton('Yüz Bul')
        
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
    def timerfunction(self):
        read,self.image = self.camera.read()
 
        height, width, channel = self.image.shape
 
        
        gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        qImg = QtGui.QImage(gray_img, width, height, width, QtGui.QImage.Format_Indexed8)

        self.lblResim.setPixmap(QtGui.QPixmap.fromImage(qImg)) 
       

        gray_img = cv2.equalizeHist(gray_img)

        qImg = QtGui.QImage(gray_img, width, height, width, QtGui.QImage.Format_Indexed8)
        self.lblResim2.setPixmap(QtGui.QPixmap.fromImage(qImg))               
        
    def resimYukle_pressed(self):
        
        self.timer.start(50)

        self.camera = cv2.VideoCapture(0)

    def filtreUygula(self):

        height, width, channel = self.image.shape
        gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray_img,100,200)

        qImg = QtGui.QImage(edges, width, height, width, QtGui.QImage.Format_Indexed8)
        self.lblResim2.setPixmap(QtGui.QPixmap.fromImage(qImg))
