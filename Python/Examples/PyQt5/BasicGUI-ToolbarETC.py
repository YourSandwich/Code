import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.statusBar().showMessage('Hier ist die StatusBar')
        exitME = QAction(QIcon('200px-Globe_icon.svg.png'), '&Exit', self)
        exitME.setShortcut('Ctrl+Q')
        exitME.setStatusTip('Exit')
        exitME.triggered.connect(self.close)

        menubar = self.menuBar()
        file = menubar.addMenu('&File') ## Das & ermöglich das drücken von alt + den ersten Buchstaben um das Menü zu öffnen
        file.addAction(exitME) ## fügt die Funktion von exitME hinzu

        toolBar = self.addToolBar('Exit')
        toolBar.addAction(exitME)

        self.setGeometry(50,50,1000,500) ## Fenstergröße und Position
        self.setWindowTitle("GUI Basic 2") ## Fenster Titel
        self.setWindowIcon(QIcon("200px-Globe_icon.svg.png")) ## Die Icon für das Fenster
        self.show()

app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())