import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

### Layouts.. Absolute, BoxLayout, QGridLayout

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        """
        Absolute Layout
        Die Buttons können sich selbst verdecken und mann muss die piexel zehlen
        upvote = QPushButton('Upvote me', self) 
        abo = QPushButton("sub me", self)
        upvote.move(20, 100)
        abo.move(50,50)
        """
        """
        GridLayout mit Taschenrechner Grid

        grid = QGridLayout()
        namen =['1','2','3','4','5','6','7','8','9']
        posis = [(i,j) for i in range(3) for j in range(3)]
        for pos, name in zip(posis,namen):
            button = QPushButton(name)
            grid.addWidget(button, *pos)

        self.setLayout(grid)
        """
        """
        BoxLayout
        
        upvote = QPushButton('Upvote me') 
        abo = QPushButton("sub me")
        h = QHBoxLayout()
        h.addWidget(upvote)
        h.addStretch(1)
        h.addWidget(upvote)
        h.addWidget(abo)

        v = QVBoxLayout()
        v.addStretch(1)
        v.addLayout(h) ## Fügt den Layout h hinzu

        self.setLayout(v)
        """
        self.setGeometry(50,50,1000,500) ## Fenstergröße und Position
        self.setWindowTitle("GUI Layout") ## Fenster Titel
        self.setWindowIcon(QIcon("200px-Globe_icon.svg.png")) ## Die Icon für das Fenster
        self.show()

app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())