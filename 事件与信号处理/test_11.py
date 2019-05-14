# -*- coding:utf8 -*-
# @TIME     :2019/5/12 21:19
# @Author   : 洪松
# @File     : test_11.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject


class Signal(QObject):
    show_mouse = pyqtSignal()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('发出自定义信号')

        self.s = Signal()
        self.s.show_mouse.connect(self.about)
        self.show()

    def about(self):
        QMessageBox.about(self, '鼠标','你点鼠标了吧！')

    def mouseMoveEvent(self, QMouseEvent):
        self.s.show_mouse.emit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())