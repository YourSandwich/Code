import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        button = QPushButton('Drück mich fest', self)
        button.move(50,50)
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("GUI Basic")
        self.setWindowIcon(QIcon("E:\Müll\Code\Python\\200px-Globe_icon.svg.png"))
        self.show()

app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())