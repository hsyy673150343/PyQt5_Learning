# -*- coding:utf8 -*-
# @TIME     :2019/5/13 21:41
# @Author   : 洪松
# @File     : test_21.py

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('工具栏')

        exit_act = QAction(QIcon('退出.png'), '退出(&E)', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('退出程序')
        exit_act.triggered.connect(qApp.quit)

        save_menu = QMenu('保存方式(&S)', self)
        save_act = QAction(QIcon('保存.png'), '保存...', self)
        save_act.setShortcut('Ctrl+S')
        save_act.setStatusTip('保存文件')
        save_as_act = QAction(QIcon('另存为.png'), '另存为...(&O)', self)
        save_as_act.setStatusTip('文件另存为')
        save_menu.addAction(save_act)
        save_menu.addAction(save_as_act)

        new_act = QAction(QIcon('新建.png'), '新建(&N)', self)
        new_act.setShortcut('Ctrl+N')
        new_act.setStatusTip('新建文件')

        men_bar = self.menuBar()
        file_menu = men_bar.addMenu('文件(&F)')
        file_menu.addAction(new_act)
        file_menu.addMenu(save_menu)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)

        tool_bar = self.addToolBar('工具栏')
        tool_bar.addAction(new_act)
        tool_bar.addAction(exit_act)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())