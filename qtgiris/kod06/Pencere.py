from PyQt5.QtWidgets import *

#AnaPencere için kendi sınıfımızı tasarlıyoruz.
class AnaPencere(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setGeometry(0,0,800,600)
        
        self.central_widget = QWidget()
        self.lblResim = QLabel("resim label",self.central_widget)

        self.btnResimYukle = QPushButton('Resim Yükle', self.central_widget)

        self.btnFiltreUygula = QPushButton('Test', self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)

        self.layout.addWidget(self.btnResimYukle)

        self.layout.addWidget(self.btnFiltreUygula)

        self.layout.addWidget(self.lblResim)

        self.setCentralWidget(self.central_widget)

        self.btnResimYukle.clicked.connect(self.resimYukle_pressed)
        self.btnFiltreUygula.clicked.connect(self.filtreUygula)
        self.show()
    def resimYukle_pressed(self):
        fileNames = QFileDialog.getOpenFileName(self,"Open Image", "./", "Image Files (*.png *.jpg *.bmp)")
        print(fileNames[0])

    def filtreUygula(self):
        print("filtreUygula")

