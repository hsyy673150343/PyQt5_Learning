# -*- coding:utf8 -*-
# @TIME     :2019/5/12 16:36
# @Author   : 洪松
# @File     : test_6_qt_entry.py

import sys
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
from 第一个PyQt5程序.test_6_qt_designer import Ui_Form
from random import randint


class my_pyqt_from(QWidget, Ui_Form):
    def __init__(self):
        super(my_pyqt_from, self).__init__()
        self.setupUi(self)
        self.num = randint(1, 100)
        self.show()

    def show_message(self):

        guess_number = int(self.lineEdit.text())
        print(self.num)

        if guess_number > self.num:
            QMessageBox.about(self, '看结果','猜大了!')
            self.lineEdit.setFocus()

        elif guess_number < self.num:
            QMessageBox.about(self, '看结果','猜小了!')
            self.lineEdit.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.lineEdit.clear()
            self.lineEdit.setFocus()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accpet()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    my_pyqt_form = my_pyqt_from()
    sys.exit(app.exec_())