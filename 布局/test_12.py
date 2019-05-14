# -*- coding:utf8 -*-
# @TIME     :2019/5/12 21:39
# @Author   : 洪松
# @File     : test_12.py

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')

        bt1 = QPushButton('剪刀',self)
        bt1.move(50,250)

        bt2 = QPushButton('石头',self)
        bt2.move(150,250)

        bt3 = QPushButton('布',self)
        bt3.move(250,250)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())