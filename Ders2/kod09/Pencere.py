
from PyQt5.QtWidgets import *

from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import cv2

#AnaPencere için kendi sınıfımızı tasarlıyoruz.
class AnaPencere(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.KameraBasladimi = False
        self.setGeometry(0,0,800,600)

        self.siniflandirici = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.gozsiniflandirici = cv2.CascadeClassifier("haarcascade_eye.xml")
        self._min_size = (30,30)

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
        
        imageshow = cv2.cvtColor(self.image,cv2.COLOR_RGB2BGR)
        
        qImg = QtGui.QImage(imageshow.data, width, height, width*3, QtGui.QImage.Format_RGB888)

        self.lblResim.setPixmap(QtGui.QPixmap.fromImage(qImg)) 

        self.gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        qImg = QtGui.QImage(self.gray_img, width, height, width, QtGui.QImage.Format_Indexed8)
        self.lblResim2.setPixmap(QtGui.QPixmap.fromImage(qImg))  
        
        
        faces = self.yuzleriBul(self.gray_img)
        gozler = self.gozleriBul(self.gray_img)
        pixmap = self.lblResim.pixmap()
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtGui.QPen(Qt.red, 5, Qt.SolidLine))
           
        
        for x,y,w,h in faces:
            painter.drawRect(x,y,w,h)
        painter.setPen(QtGui.QPen(Qt.yellow, 5, Qt.SolidLine))
        for x,y,w,h in gozler:
            painter.drawRect(x,y,w,h)
        
        self.KameraBasladimi = True             
        
    def resimYukle_pressed(self):
        self.camera = cv2.VideoCapture(0)
        self.timer.start(50)
       

        
    def yuzleriBul(self,gray_img):

        gray_img = cv2.equalizeHist(gray_img)

        faces = self.siniflandirici.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=4,flags=cv2.CASCADE_SCALE_IMAGE,minSize=self._min_size)
        return faces
    def gozleriBul(self,gray_img):
        gray_img = cv2.equalizeHist(gray_img)

        faces = self.gozsiniflandirici.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=4,flags=cv2.CASCADE_SCALE_IMAGE,minSize=self._min_size)
        return faces
    def filtreUygula(self):

        height, width, channel = self.image.shape
        gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray_img,100,200)

        qImg = QtGui.QImage(edges, width, height, width, QtGui.QImage.Format_Indexed8)
        self.lblResim2.setPixmap(QtGui.QPixmap.fromImage(qImg))
