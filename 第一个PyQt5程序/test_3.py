# -*- coding:utf8 -*-
# @TIME     :2019/5/12 14:18
# @Author   : 洪松
# @File     : test_3.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)
    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = " ".join(sys.argv[1:])
    except ValueError:
        title = "通过命令行改窗口标题"

    w = QWidget()
    w.resize(500, 300)
    w.move(300, 300)
    w.setWindowTitle(title)
    w.show()

    sys.exit(app.exec_())