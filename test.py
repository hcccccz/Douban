from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        w = W()
        global w1
        w1 = QLabel("nt")
        self.setCentralWidget(w)
        self.setGeometry(1000,500,600,600)
        self.show()
        w.destroyed.connect(self.set)
    def set(self):
        
        self.setCentralWidget(w1)

class W(QWidget):

    def __init__(self):
        super().__init__()
        self.ui()
    def ui(self):
        label = QLabel("hi",self)
        label.move(250,250)
        btn = QPushButton("ex",self)
        btn.move(400,400)
        btn.clicked.connect(self.shift)
    def shift(self):
        self.deleteLater()

app = QApplication([])
window = Window()
app.exec_()
