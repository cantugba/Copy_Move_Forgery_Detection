import tkinter as tk # tkinter dosya işlemleri için
from Detector.AkazeDetector import AkazeDetector
from Detector.SiftDetector import SiftDetector
from Detector.SurfDetector import SurfDetector
from PyQt5 import QtGui, QtWidgets, QtCore
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image
import numpy as np
from Singleton import SingletonMeta


class Facade(metaclass=SingletonMeta):

    # boyut, resmi yeniden boyutlandırmak için stajyer numarasıdır, resim aynı en boy oranı korunarak yeniden boyutlandırılır
    # numpy Resim gösterimi ve yedeklenen resmi geri alma
    size = 500
    NPundo = np.empty((2, 2))
    NPimg = np.empty((2, 2))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 617)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                 "selection-background-color: rgb(135, 171, 255);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setStyleSheet("QLabel{ background-color : rgb(204, 231, 232); color : black; }")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(1, 5, 636, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon)
        self.actionUndo.setObjectName("actionUndo")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSurf = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/surf.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSurf.setIcon(icon2)
        self.actionSurf.setObjectName("actionSurf")

        self.actionAkaze = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/akaze.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAkaze.setIcon(icon4)
        self.actionAkaze.setObjectName("actionAkaze")

        self.actionSift = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/sift.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSift.setIcon(icon8)
        self.actionSift.setObjectName("actionSift")

        self.actionZoomIn = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon9)
        self.actionZoomIn.setObjectName("actionZoomIn")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionZoomOut = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon10)
        self.actionZoomOut.setObjectName("actionZoomOut")

        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionSurf)
        self.toolBar.addAction(self.actionAkaze)
        self.toolBar.addAction(self.actionSift)
        self.toolBar.addAction(self.actionZoomIn)
        self.toolBar.addAction(self.actionZoomOut)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CMDF"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))

        self.toolBar.setWindowTitle(_translate("MainWindow", "İşlemler"))

        self.actionOpen.setText(_translate("MainWindow", "Resim Seç"))

        self.actionUndo.setText(_translate("MainWindow", "Geri Al"))
        self.actionUndo.setToolTip(_translate("MainWindow", "Resmi Sıfırla"))

        self.actionSave.setText(_translate("MainWindow", "Kaydet"))

        self.actionSurf.setText(_translate("MainWindow", "SURF"))
        self.actionSurf.setToolTip(_translate("MainWindow", "Surf Tabanlı Tespit."))

        self.actionAkaze.setText(_translate("MainWindow", "AKAZE"))
        self.actionAkaze.setToolTip(_translate("MainWindow", "Akaze Tabanlı Tespit."))

        self.actionSift.setText(_translate("MainWindow", "SIFT"))
        self.actionSift.setToolTip(_translate("MainWindow", "Sift Tabanlı Tespit."))

        self.actionZoomIn.setText(_translate("MainWindow", "Yakınlaştır"))
        self.actionZoomIn.setToolTip(_translate("MainWindow", "Resmi Yakınlaştır"))

        self.actionExit.setText(_translate("MainWindow", "Çıkış"))
        self.actionExit.setToolTip(_translate("MainWindow", "Programı Sonlandır."))

        self.actionZoomOut.setText(_translate("MainWindow", "Uzaklaştır"))
        self.actionZoomOut.setToolTip(_translate("MainWindow", "Resmi Uzaklaştır"))

        # buton bağlantıları

        self.actionOpen.triggered.connect(self.OpenImage)
        self.actionAkaze.triggered.connect(self.AKAZE)
        self.actionSift.triggered.connect(self.SIFT)
        self.actionUndo.triggered.connect(self.undo)
        self.actionExit.triggered.connect(self.exitp)
        self.actionSurf.triggered.connect(self.SURF)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionZoomIn.triggered.connect(self.zoomIn)
        self.actionSave.triggered.connect(self.saveImage)

    # programı sonlandır
    def exitp(self):
        exit()

    # yapılan işlemi geri al
    def undo(self):
        self.image = self.origImage.copy()
        self.showImage(self.image)

    # önceki işlemden önce yedekleme
    def backup(self):
        self.NPundo = self.NPimg

    # resmi yakınlaştır
    def zoomIn(self):
        self.size = int(self.size * 1.2)
        self.showImage(self.image)

    # resmi uzaklaştır
    def zoomOut(self):
        self.size = int(self.size / 1.2)
        self.showImage(self.image)

    def SIFT(self):
        sift = SiftDetector(self.image)
        self.image = sift.image
        self.showImage(self.image)

    def AKAZE(self):
        akaze = AkazeDetector(self.image)
        self.image = akaze.image
        self.showImage(self.image)

    def SURF(self):
        surf = SurfDetector(self.image)
        self.image = surf.image
        self.showImage(self.image)

    def OpenImage(self):
        self.backup()
        root = tk.Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="~/PycharmProjects/Bitirme/Test-Images",
                                                   title="Dosya Seç",
                                                   filetypes=(("jpeg files", "*.jpeg"), ("all files", "*.*")))
        if root.filename:
            # img = Image.open(root.filename)
            self.image = cv2.imread(root.filename, cv2.IMREAD_COLOR)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.origImage = self.image.copy()
            self.showImage(self.origImage)

    # resmi kaydederken rengi bozuluyor düzenlenecek
    def saveImage(self):
        root = tk.Tk()
        root.withdraw()
        root.filename = filedialog.asksaveasfilename(initialdir="~/PycharmProjects/Bitirme/Results",
                                                     title="Resmi Kaydet",
                                                     filetypes=(("jpeg files", "*.jpeg"), ("all files", "*.*")))
        if root.filename:
            try:
                saveIMG = Image.fromarray(self.NPimg.astype('uint8'))
                saveIMG.save(root.filename)
            except ValueError:
                saveIMG = Image.fromarray(self.NPimg.astype('uint8'))
                saveIMG.save(root.filename + '.png')


    # Qt etiketindeki görüntüyü gösterir, boyut self.size'den türetilir (daha büyük ve daha küçük olarak değiştirilebilir)
    def showImage(self, NPimgShow):
        image_profile = QtGui.QImage(NPimgShow, NPimgShow.shape[1], NPimgShow.shape[0], NPimgShow.shape[1] * 3,
                                     QtGui.QImage.Format_RGB888)  # QImage object
        image_profile = image_profile.scaled(self.size, self.size, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                             transformMode=QtCore.Qt.SmoothTransformation)  # görüntüyü ölçeklendirmek ve En Boy Oranını korumak için
        self.label.setPixmap(QtGui.QPixmap.fromImage(image_profile))
