from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import json
class Login_inG(QMainWindow):


    def __init__(self):
        self.account = "" #登录
        self.password = "" #登录

        super().__init__()

        self.ui()
        self.button_0.clicked.connect(self.pressEvent_get0)
        self.button.clicked.connect(self.pressEvent_login)
    def ui(self):

        layout_v = QVBoxLayout()
        layout_f = QFormLayout()
        layout_h = QHBoxLayout()

        self.account_edit = QLineEdit(self)
        account = QLabel("账号")
        layout_f.addRow(account,self.account_edit)
        password = QLabel("密码")
        self.password_edit = QLineEdit(self)
        layout_f.addRow(password,self.password_edit)

        self.button_0 = QPushButton("Get token")
        self.button = QPushButton("Log in")
        layout_v.addStretch(2)
        layout_v.addLayout(layout_f)
        layout_h.addStretch(1)
        layout_h.addWidget(self.button_0)
        layout_h.addWidget(self.button)
        layout_h.addStretch(1)


        layout_v.addLayout(layout_h)
        layout_v.addStretch(1)
        self.w = QWidget()
        self.w.setLayout(layout_v)
        self.setCentralWidget(self.w)
        self.setGeometry(1080,700,500,400)
        self.show()
        self.setWindowTitle("豆瓣FM")
    def token_get(self):
        data = {"apikey": "02646d3fb69a52ff072d47bf23cef8fd",
                "client_id": "02646d3fb69a52ff072d47bf23cef8fd",
                "client_secret": "cde5d61429abcd7c",
                "udid": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "douban_udid": "b635779c65b816b13b330b68921c0f8edc049590",
                "device_id": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "grant_type": "password",
                "redirect_uri": "http://www.douban.com/mobile/fm",
                "username": self.account,
                "password": self.password,
                }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = json.loads(requests.post("https://www.douban.com/service/auth2/token", data = data, headers = headers).text)
        with open("token.txt", "w") as f:
            info = {}
            info["username"] = response["douban_user_name"]
            info["token"] = "Bearer " + response["access_token"]
            info["expire"] = response["expires_in"]
            f.write(str(info))


    def request(self):

        data = {"alt": "json",
                "app_name": "radio_iphone",
                "apikey": "02646d3fb69a52ff072d47bf23cef8fd",
                "client": "s:mobile|y:iOS 10.2|f:115|d:b88146214e19b8a8244c9bc0e2789da68955234d|e:iPhone7,1|m:appstore",
                "client_id": "02646d3fb69a52ff072d47bf23cef8fd",
                "icon_cate": "xlarge",
                "udid": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "douban_udid": "b635779c65b816b13b330b68921c0f8edc049590",
                "version": 115,
                }
        with open("token.txt", "r") as f:
            info = eval(f.read())
        headers = {"Authorization": info["token"]}
        with open("request.txt", "w") as f:
            response = json.loads(requests.get(Channel.channel_url, params = data, headers = headers ).text)['groups']
            f.write(str(response))

    def set_info(self,account,password):
        self.account = account
        self.password = password

    def pressEvent_get0(self):

        if self.account_edit.text() == "" or self.password_edit.text() == "":
            message = QMessageBox(self)
            message.setText("账号密码需要！")
            message.exec_()
        else:
            self.set_info(self.account_edit.text(),self.password_edit.text())
            self.token_get()
            message = QMessageBox(self)
            message.setText("token saved")
            message.exec_()

    def pressEvent_login(self,channel):
        if self.account_edit.text() == "" or self.password_edit.text() == "":
            message = QMessageBox(self)
            message.setText("账号密码需要！")
            message.exec_()
        else:
            self.set_info(self.account_edit.text(),self.password_edit.text())
            self.request()
        self.w.deleteLater()
        channel = Channel()
        self.setCentralWidget(channel)




class Channel(QWidget):
    channel_url = "https://api.douban.com/v2/fm/app_channels"
    song_url = "https://api.douban.com/v2/fm/playlist"

    def __init__(self):

        super().__init__()


        self.ui()
    def ui(self):
        self.setWindowTitle("豆瓣FM")
        self.setGeometry(1080,700,500,400)
        choices = self.group()
        btns = [QPushButton(choices[i]["name"]) for i in range(len(choices))]

        layout_v = QVBoxLayout()
        for idx in range(len(btns)):
            layout_v.addWidget(btns[idx])

        self.setStyleSheet(open_sheet("style.css"))

        self.setLayout(layout_v)


    def group(self):

        data = eval(open("request.txt","r").read())
        choices = list()
        for idx in range(len(data)):
            if idx == 0:
                choice = dict()
                choice['name'] = "我的私人"
                choice['value'] = data[idx]['group_id']
                choices.append(choice)
            else:
                choice = dict()
                choice['name'] = data[idx]['group_name']
                choice['value'] = data[idx]['group_id']
                choices.append(choice)
        return choices







def open_sheet(filename:str):
    with open(filename,"r") as f:

        return f.read()



if __name__ == "__main__":


    app = QApplication([])
    login_inG = Login_inG()

    app.exec_()
