# -*- coding:utf8 -*-
# @TIME     :2019/5/12 21:56
# @Author   : 洪松
# @File     : test_14.py


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')

    def init_ui(self):
        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        h_box = QHBoxLayout()
        h_box.addStretch(1) #增加伸缩量
        h_box.addWidget(bt1)
        h_box.addStretch(1)#增加伸缩量
        h_box.addWidget(bt2)
        h_box.addStretch(1)#增加伸缩量
        h_box.addWidget(bt3)
        h_box.addStretch(6)#增加伸缩量

        self.setLayout(h_box)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())