from douban.requ import Log_in
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Color(QWidget):

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout1 = QVBoxLayout()
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout1.addWidget(Color('green'))
        layout1.addWidget(Color('blue'))
        widget = QWidget()
        widget.setLayout(layout)
        widget1 = QWidget()
        widget1.setLayout(layout1)
        layoutf = QHBoxLayout()
        layout1.addWidget(Color('red'))
        layoutf.addWidget(widget)
        layoutf.addWidget(widget1)
        layoutf.setSpacing(200)
        widgetf = QWidget()
        widgetf.setLayout(layoutf)
        self.setCentralWidget(widgetf)
        self.setGeometry(400,400,450,500)
        self.show()
app = QApplication([])
ex = Window()
app.exec_()
