# -*- coding:utf8 -*-
# @TIME     :2019/5/12 14:41
# @Author   : 洪松
# @File     : test_5.py


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Icon(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('我的界面+草莓')
        self.setWindowIcon(QIcon('草莓.png'))

        btn = QPushButton('退出', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(70,30)
        btn.move(50, 50)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Icon()
    sys.exit(app.exec_())