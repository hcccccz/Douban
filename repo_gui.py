from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Login_win(QWidget):

    def __init__(self):
        super().__init__()
        self.ui()
    def ui(self):
        layout_v = QVBoxLayout()
        layout_f = QFormLayout()
        layout_h = QHBoxLayout()

        account_edit = QLineEdit(self)
        account = QLabel("账号")
        layout_f.addRow(account,account_edit)
        password = QLabel("密码")
        password_edit = QLineEdit(self)
        layout_f.addRow(password,password_edit)


        button = QPushButton("Log in")
        layout_v.addStretch(2)
        layout_v.addLayout(layout_f)
        layout_h.addStretch(1)
        layout_h.addWidget(button)
        layout_h.addStretch(1)


        layout_v.addLayout(layout_h)
        layout_v.addStretch(1)

        self.setLayout(layout_v)
        self.setGeometry(500,1000,500,400)
        self.show()
        self.setWindowTitle("豆瓣FM")





app = QApplication([])
login_win = Login_win()
app.exec_()
