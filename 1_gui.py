from douban.requ import Log_in
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout1 = QGridLayout()
        layout.setContentsMargins(10,50,10,10)
        self.btn_l = list()
        for n in range(1,10):
            self.btn_l.insert(n-1,QPushButton(str(n)))
        for idx in range(len(self.btn_l)):
            if idx <= 2:
                layout1.addWidget(self.btn_l[idx], 0, idx)
            elif 2< idx <= 5:
                layout1.addWidget(self.btn_l[idx], 1, idx-3)
            else:
                layout1.addWidget(self.btn_l[idx], 2, idx-6)
        self.btn_l.append(QPushButton("0"))
        self.btn_l.append(QPushButton(b"\xc3\xb7".decode("utf8")))
        self.btn_l.append(QPushButton("*"))
        self.btn_l.append(QPushButton("."))
        self.btn_l.append(QPushButton("="))
        self.btn_l.append(QPushButton("+"))
        self.btn_l.append(QPushButton("-"))
        self.line = QLineEdit()
        self.line.setTextMargins(20,20,20,20)
        layout.addWidget(self.line)
        layout.addStretch()
        layout1.addWidget(button_pls, 0, 3)
        layout1.addWidget(button_min, 1, 3)
        layout1.addWidget(button_ti, 2, 3)
        layout1.addWidget(button_di, 3, 3)
        layout1.addWidget(button0, 3, 0)
        layout1.addWidget(button_eq, 3, 2)
        layout1.addWidget(button_poi, 3, 1)
        layout.addLayout(layout1)
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.setGeometry(400,400,600,500)

app = QApplication([])
ex = Window()
ex.show()
app.exec_()
