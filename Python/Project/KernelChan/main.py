from PySide2.QtWidgets import QApplication,QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KernelChan")
        self.setGeometry(300,300,300,300)

App = QApplication(sys.argv)
window = Window()
window.show()

App.exec_()
sys.exit(0)