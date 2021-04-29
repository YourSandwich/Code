from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox
from PySide2.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KernelChan")
        self.setGeometry(300,300,300,300)

        self.setIcon()
        self.setButton()

    def setIcon(self):
        appIcon = QIcon('icon.png')
        self.setWindowIcon(appIcon)

    def setButton(self):
        button = QPushButton("Exit", self)
        button.move(190,240)

        button.clicked.connect(self.exitApp)

    def exitApp(self):
        askUser = QMessageBox.question(self, "Quit", "Are you Sure?", QMessageBox.Yes | QMessageBox.No)

        if askUser == QMessageBox.Yes:
            App.quit()
        elif askUser == QMessageBox.No:
            pass

App = QApplication(sys.argv)
window = Window()
window.show()

App.exec_()
sys.exit(0)
