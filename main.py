
from PyQt5 import QtWidgets

from SingletonGui import Ui_MainWindow

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    u2 = Ui_MainWindow()

    #singleton test
    if id(ui) == id(u2):
        print("Singleton çalışır, her iki değişken de aynı örneği içerir")

    else:
        print("birden fazla örnek, singleton çalışmadı")

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


