# -*- coding:utf8 -*-
# @TIME     :2019/5/12 14:01
# @Author   : 洪松
# @File     : test_2.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 300)
    w.move(300, 300)
    w.setWindowTitle('我的第一个PyQt5小程序')
    w.show()

    sys.exit(app.exec_())
