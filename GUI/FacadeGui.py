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
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(1, 5, 636, 21))
        self.menu_bar.setObjectName("menubar")
        self.q_menu = QtWidgets.QMenu(self.menu_bar)
        self.q_menu.setObjectName("menuMenu")
        main_window.setMenuBar(self.menu_bar)
        self.tool_bar = QtWidgets.QToolBar(main_window)
        self.tool_bar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tool_bar.setObjectName("toolBar")
        main_window.addToolBar(QtCore.Qt.LeftToolBarArea, self.tool_bar)
        self.action_Open = QtWidgets.QAction(main_window)
        self.action_Open.setObjectName("actionOpen")
        self.action_Undo = QtWidgets.QAction(main_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Undo.setIcon(icon)
        self.action_Undo.setObjectName("actionUndo")
        self.action_Save = QtWidgets.QAction(main_window)
        self.action_Save.setObjectName("actionSave")
        self.action_Surf = QtWidgets.QAction(main_window)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/surf.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Surf.setIcon(icon1)
        self.action_Surf.setObjectName("actionSurf")
        self.action_Akaze = QtWidgets.QAction(main_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/akaze.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Akaze.setIcon(icon2)
        self.action_Akaze.setObjectName("actionAkaze")
        self.action_Sift = QtWidgets.QAction(main_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/sift.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sift.setIcon(icon3)
        self.action_Sift.setObjectName("actionSift")
        self.action_ZoomIn = QtWidgets.QAction(main_window)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ZoomIn.setIcon(icon4)
        self.action_ZoomIn.setObjectName("actionZoomIn")
        self.action_Exit = QtWidgets.QAction(main_window)
        self.action_Exit.setObjectName("actionExit")
        self.action_ZoomOut = QtWidgets.QAction(main_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ZoomOut.setIcon(icon5)
        self.action_ZoomOut.setObjectName("actionZoomOut")
        self.q_menu.addAction(self.action_Open)
        self.q_menu.addAction(self.action_Save)
        self.q_menu.addAction(self.action_Exit)
        self.menu_bar.addAction(self.q_menu.menuAction())
        self.tool_bar.addAction(self.action_Undo)
        self.tool_bar.addAction(self.action_Surf)
        self.tool_bar.addAction(self.action_Akaze)
        self.tool_bar.addAction(self.action_Sift)
        self.tool_bar.addAction(self.action_ZoomIn)
        self.tool_bar.addAction(self.action_ZoomOut)
        self.translateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "CMDF"))
        self.q_menu.setTitle(_translate("MainWindow", "Menu"))
        self.tool_bar.setWindowTitle(_translate("MainWindow", "İşlemler"))
        self.action_Open.setText(_translate("MainWindow", "Resim Seç"))
        self.action_Undo.setText(_translate("MainWindow", "Resmi Sıfırla"))
        self.action_Undo.setToolTip(_translate("MainWindow", "Yapılan İşlemleri Geri Al"))
        self.action_Save.setText(_translate("MainWindow", "Kaydet"))
        self.action_Surf.setText(_translate("MainWindow", "SURF"))
        self.action_Surf.setToolTip(_translate("MainWindow", "Surf Tabanlı Tespit."))
        self.action_Akaze.setText(_translate("MainWindow", "AKAZE"))
        self.action_Akaze.setToolTip(_translate("MainWindow", "Akaze Tabanlı Tespit."))
        self.action_Sift.setText(_translate("MainWindow", "SIFT"))
        self.action_Sift.setToolTip(_translate("MainWindow", "Sift Tabanlı Tespit."))
        self.action_ZoomIn.setText(_translate("MainWindow", "Yakınlaştır"))
        self.action_ZoomIn.setToolTip(_translate("MainWindow", "Resmi Yakınlaştır"))
        self.action_Exit.setText(_translate("MainWindow", "Çıkış"))
        self.action_Exit.setToolTip(_translate("MainWindow", "Programı Sonlandır."))
        self.action_ZoomOut.setText(_translate("MainWindow", "Uzaklaştır"))
        self.action_ZoomOut.setToolTip(_translate("MainWindow", "Resmi Uzaklaştır"))

        # buton bağlantıları

        self.action_Open.triggered.connect(self.openImage)
        self.action_Akaze.triggered.connect(self.akazeDetector)
        self.action_Sift.triggered.connect(self.siftDetector)
        self.action_Undo.triggered.connect(self.undo)
        self.action_Exit.triggered.connect(self.exit)  # programı sonlandır
        self.action_Surf.triggered.connect(self.surfDetector)
        self.action_ZoomOut.triggered.connect(self.zoomOut)
        self.action_ZoomIn.triggered.connect(self.zoomIn)
        self.action_Save.triggered.connect(self.saveImage)

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

    def openImage(self):
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

    def siftDetector(self):
        sift = SiftDetector(self.image)
        self.image = sift.image
        self.showImage(self.image)

    def akazeDetector(self):
        akaze = AkazeDetector(self.image)
        self.image = akaze.image
        self.showImage(self.image)

    def surfDetector(self):
        surf = SurfDetector(self.image)
        self.image = surf.image
        self.showImage(self.image)