from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KernelChan")
        self.setGeometry(300,300,300,300)

        self.center()
        self.setIcon()
        self.setButton("Install",100,240,None)
        self.setButton("Exit",190,240,self.exitApp)

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def setIcon(self):
        appIcon = QIcon('icon.png')
        self.setWindowIcon(appIcon)

    def setButton(self, name, x, y,function):
        button = QPushButton(name, self)
        button.move(x,y)

        button.clicked.connect(function)

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
