import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *


class EigenerEvent(QObject):   ## Erstellt ein event (Signal)
    schliesmichEvent = pyqtSignal()


class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.sig = EigenerEvent()
        self.sig.schliesmichEvent.connect(self.close) ## die funktion von schliesmichEvent
        QToolTip.setFont(QFont('Arial', 13))
        button = QPushButton('Drück mich fest', self)
        schliesen = QPushButton('Exit', self)
        button.move(50,50)
        schliesen.move(50,100)
        button.setToolTip('Mein <b>Knopf</b>') ## Hover Effekt
        button.clicked.connect(self.gedrueckt) ## was passieren soll wenn das obiekt button gedrückt wird ->>> button dann die aktion und connect ist immer da zum schluss die Funktion
                                               ## Andere Events wehren pressed und released was also bei klciken oder losslasen passiert
        schliesen.clicked.connect(QtCore.QCoreApplication.instance().quit) ## Schliest die Application

       #self.setToolTip("Magissskku") ## self sorgt dafür das überall die Funktion setToolTip übernommen wird.
        self.setGeometry(50,50,500,500) ## Fenstergröße und Position
        self.setWindowTitle("GUI Basic") ## Fenster Titel
        self.setWindowIcon(QIcon("E:\Müll\Code\Python\\200px-Globe_icon.svg.png")) ## Die Icon für das Fenster
        self.show()

    def gedrueckt(self):
        sender = self.sender()
        sender.move(200,100)
        print(sender.text() + "Knopf betätigt")

    def keyPressEvent(self, QKeyEvent): ### überschreibt ein event --> wenn W gedrückt wird soll die Anwendung geschlossen werden
        if QKeyEvent.key() == Qt.Key_W: ##  Was passiert wenn W gedrückt wird
            self.sig.schliesmichEvent.emit() ##emit() für signal senden

app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())