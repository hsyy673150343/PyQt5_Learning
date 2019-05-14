# -*- coding:utf8 -*-
# @TIME     :2019/5/13 20:28
# @Author   : 洪松
# @File     : test_18.py


from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui_init()

    def gui_init(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('简单的菜单')

        exit_act = QAction(QIcon('退出.png'), '退出(&E)', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('退出程序')
        exit_act.triggered.connect(qApp.quit)

        meu_bar = self.menuBar()
        file_menu = meu_bar.addMenu('文件(&F)')
        file_menu.addAction(exit_act)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())