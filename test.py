from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        media = QMediaPlayer(self,QMediaPlayer.StreamPlayback)
        #media.setPlaylist()
        self.show()
        self.setCentralWidget(media)
        self.setGeometry(400,400,450,450)





if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec_()
