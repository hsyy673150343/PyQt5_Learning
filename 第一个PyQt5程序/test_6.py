# -*- coding:utf8 -*-
# @TIME     :2019/5/12 16:33
# @Author   : 洪松
# @File     : test_6.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.num = randint(1, 100)
        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('猜数字')
        self.setWindowIcon(QIcon('草莓.png'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(self.show_message)

        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def show_message(self):

        guess_number = int(self.text.text())
        print(self.num)

        if guess_number > self.num:
            QMessageBox.about(self, '看结果','猜大了!')
            self.text.setFocus()
        elif guess_number < self.num:
            QMessageBox.about(self, '看结果','猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accpet()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())