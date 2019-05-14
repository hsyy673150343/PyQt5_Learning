# -*- coding:utf8 -*-
# @TIME     :2019/5/13 20:23
# @Author   : 洪松
# @File     : test_17.py

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.statusBar().showMessage('准备就绪')
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('状态栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())