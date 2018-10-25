
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *




class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

        button_group = QButtonGroup()


    def init_ui(self):
        layout_v = QVBoxLayout()
        layout_g = QGridLayout()
        layout_v.setContentsMargins(10,50,10,10)


        button0 = QPushButton("0")
        button0.clicked.connect(lambda:self.inputEvent(button0))  #callable object only
        layout_g.addWidget(button0, 3, 0)

        button1 = QPushButton("1")
        layout_g.addWidget(button1, 0, 0)
        button1.clicked.connect(lambda:self.inputEvent(button1))

        button2 = QPushButton("2")
        layout_g.addWidget(button2, 0, 1)
        button2.clicked.connect(lambda:self.inputEvent(button2))

        button3 = QPushButton("3")
        layout_g.addWidget(button3, 0, 2)
        button3.clicked.connect(lambda:self.inputEvent(button3))

        button4 = QPushButton("4")
        layout_g.addWidget(button4, 1, 0)
        button4.clicked.connect(lambda:self.inputEvent(button4))

        button5 = QPushButton("5")
        layout_g.addWidget(button5, 1, 1)
        button5.clicked.connect(lambda:self.inputEvent(button5))

        button6 = QPushButton("6")
        layout_g.addWidget(button6, 1, 2)
        button6.clicked.connect(lambda:self.inputEvent(button6))

        button7 = QPushButton("7")
        layout_g.addWidget(button7, 2, 0)
        button7.clicked.connect(lambda:self.inputEvent(button7))

        button8 = QPushButton("8")
        layout_g.addWidget(button8, 2, 1)
        button8.clicked.connect(lambda:self.inputEvent(button8))

        button9 = QPushButton("9")
        layout_g.addWidget(button9, 2, 2)
        button9.clicked.connect(lambda:self.inputEvent(button9))

        button_di = QPushButton(b"\xc3\xb7".decode("utf8"))
        layout_g.addWidget(button_di, 3, 3)
        button_di.clicked.connect(lambda:self.inputEvent(button_di))

        button_ti = QPushButton("*")
        layout_g.addWidget(button_ti, 2, 3)
        button_ti.clicked.connect(lambda:self.inputEvent(button_ti))

        button_poi = QPushButton(".")
        layout_g.addWidget(button_poi, 3, 1)
        button_poi.clicked.connect(lambda:self.inputEvent(button_poi))

        button_eq = QPushButton("=")
        layout_g.addWidget(button_eq, 3, 2)
        button_eq.clicked.connect(lambda:self.inputEvent(button_eq))

        button_pls = QPushButton("+")
        layout_g.addWidget(button_pls, 0, 3)
        button_pls.clicked.connect(lambda:self.inputEvent(button_pls))

        button_min = QPushButton("-")
        layout_g.addWidget(button_min, 1, 3)
        button_min.clicked.connect(lambda:self.inputEvent(button_min))


        self.line = QLineEdit()
        self.line.setTextMargins(20,20,20,20)
        layout_v.addWidget(self.line)
        layout_v.addStretch()
        layout_v.addLayout(layout_g)
        w = QWidget()
        w.setLayout(layout_v)
        self.setCentralWidget(w)
        self.setGeometry(400,400,600,500)
    def inputEvent(self,button):
        if button.text() != "=":
            self.line.insert(button.text())
        else:
            try:
                answer = eval(self.line.text())
                self.line.setText(str(answer))
            except:
                self.line.setText(str("Input is invalid"))



app = QApplication([])
ex = Window()
ex.show()
app.exec_()
