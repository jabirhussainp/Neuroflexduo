from PyQt5 import QtWidgets, uic
import sys
from db import MainWindow123
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Final.ui', self)
        self.setWindowTitle('NeuroFlex Duo')

        self.anew = self.findChild(QtWidgets.QAction, 'actionNew')
        self.anew.triggered.connect(self.openWindow)
        self.anew.setShortcut('Ctrl+N')
        self.aopen = self.findChild(QtWidgets.QAction, 'actionOpen')
        self.aopen.triggered.connect(self.openWindow)
        self.aopen.setShortcut('Ctrl+O')
        self.aexit = self.findChild(QtWidgets.QAction, 'actionExit')
        self.aexit.triggered.connect(self.exitWindow)
        self.aexit.setShortcut('Alt+F4')

        self.show()

    def openWindow(self):
        self.openwndw = MainWindow123()
        self.openwndw.show()

    def exitWindow(self):
        app.exit()




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()




