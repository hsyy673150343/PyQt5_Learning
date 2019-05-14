# -*- coding:utf8 -*-
# @TIME     :2019/5/12 21:45
# @Author   : 洪松
# @File     : test_13.py

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('箱式布局')
        self.init_ui()

    def init_ui(self):
        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        h_box = QHBoxLayout()
        h_box.addStretch(1)
        h_box.addWidget(bt1)
        h_box.addWidget(bt2)
        h_box.addWidget(bt3)

        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())