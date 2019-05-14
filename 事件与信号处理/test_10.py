# -*- coding:utf8 -*-
# @TIME     :2019/5/12 21:04
# @Author   : 洪松
# @File     : test_10.py

import sys
from PyQt5.QtWidgets import (QApplication, QMessageBox, QWidget, QPushButton)
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('石头剪刀布小游戏')

        bt1 = QPushButton('剪刀', self)
        bt1.setGeometry(30, 180, 50, 50)

        bt2 = QPushButton('石头', self)
        bt2.setGeometry(100, 180, 50, 50)

        bt3 = QPushButton('布', self)
        bt3.setGeometry(170, 180, 50, 50)

        bt1.clicked.connect(self.button_clicked)
        bt2.clicked.connect(self.button_clicked)
        bt3.clicked.connect(self.button_clicked)

        self.player = 0
        self.computer = randint(1,3)
        self.show()

    def button_clicked(self):
        sender = self.sender()
        if sender.text() == '剪刀':
            self.player = 1
        elif sender.text() == '石头':
            self.player = 2
        else:
            self.player = 3

        if self.player == self.computer:
            QMessageBox.about(self, '结果', '平手')
        elif self.player == 1 and self.computer == 2:
            QMessageBox.about(self, '结果', '电脑：石头，电脑赢了！')
        elif self.player == 2 and self.computer == 3:
            QMessageBox.about(self, '结果', '电脑：布，电脑赢了！')
        elif self.player == 3 and self.computer == 1:
            QMessageBox.about(self, '结果', '电脑：剪刀，电脑赢了！')
        elif self.computer == 1 and self.player == 2:
            QMessageBox.about(self, '结果', '电脑：剪刀，玩家赢了！')
        elif self.computer == 2 and self.player == 3:
            QMessageBox.about(self, '结果', '电脑：石头，玩家赢了！')
        elif self.computer == 3 and self.player == 1:
            QMessageBox.about(self, '结果', '电脑：布，玩家赢了！')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())