import cv2
import numpy as np
import tkinter as tk  # tkinter dosya işlemleri için
from tkinter import *
from PIL import Image
from tkinter import filedialog
from PyQt5 import QtGui, QtWidgets, QtCore
from Detector.AkazeDetector import AkazeDetector
from Detector.SiftDetector import SiftDetector
from Detector.SurfDetector import SurfDetector
from GUI.Singleton import SingletonMeta


class Facade(metaclass=SingletonMeta):
    # boyut, resmi yeniden boyutlandırmak için stajyer numarasıdır, resim aynı en boy oranı korunarak yeniden boyutlandırılır
    # numpy Resim gösterimi ve yedeklenen resmi geri alma
    size = 720
    NPundo = np.empty((2, 2))
    NPimg = np.empty((2, 2))

    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(720, 720)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        main_window.setMouseTracking(False)
        main_window.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                  "selection-background-color: rgb(135, 171, 255);\n"
                                  "background-color: rgb(255, 255, 255);\n")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setStyleSheet("QLabel{ background-color : rgb(204, 231, 232); color : black; }")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(1, 5, 636, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        main_window.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(main_window)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        main_window.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(main_window)
        self.actionOpen.setObjectName("actionOpen")
        self.actionUndo = QtWidgets.QAction(main_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon)
        self.actionUndo.setObjectName("actionUndo")
        self.actionSave = QtWidgets.QAction(main_window)
        self.actionSave.setObjectName("actionSave")
        self.actionSurf = QtWidgets.QAction(main_window)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/surf.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSurf.setIcon(icon1)
        self.actionSurf.setObjectName("actionSurf")
        self.actionAkaze = QtWidgets.QAction(main_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/akaze.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAkaze.setIcon(icon2)
        self.actionAkaze.setObjectName("actionAkaze")
        self.actionSift = QtWidgets.QAction(main_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/sift.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSift.setIcon(icon3)
        self.actionSift.setObjectName("actionSift")
        self.actionZoomIn = QtWidgets.QAction(main_window)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon4)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionExit = QtWidgets.QAction(main_window)
        self.actionExit.setObjectName("actionExit")
        self.actionZoomOut = QtWidgets.QAction(main_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon5)
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
        self.translateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "CMDF"))
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
        self.actionExit.triggered.connect(self.exit)  # programı sonlandır
        self.actionSurf.triggered.connect(self.SURF)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionZoomIn.triggered.connect(self.zoomIn)
        self.actionSave.triggered.connect(self.saveImage)

    def exit(self):
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
                save_img = Image.fromarray(self.NPimg.astype('uint8'))
                save_img.save(root.filename)
            except ValueError:
                save_img = Image.fromarray(self.NPimg.astype('uint8'))
                save_img.save(root.filename + '.png')

    # Qt etiketindeki görüntüyü gösterir, boyut self.size'den türetilir (daha büyük ve daha küçük olarak değiştirilebilir)

    def showImage(self, img_show):
        image_profile = QtGui.QImage(img_show, img_show.shape[1], img_show.shape[0], img_show.shape[1] * 3,
                                     QtGui.QImage.Format_RGB888)  # QImage object
        image_profile = image_profile.scaled(self.size, self.size, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                             transformMode=QtCore.Qt.SmoothTransformation)   # görüntüyü ölçeklendirmek ve En Boy Oranını korumak için
        self.label.setPixmap(QtGui.QPixmap.fromImage(image_profile))
