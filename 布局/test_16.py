# -*- coding:utf8 -*-
# @TIME     :2019/5/13 19:44
# @Author   : 洪松
# @File     : test_16.py

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('表单布局')
        self.ui_init()

    def ui_init(self):
        form_layout = QFormLayout()
        name_label = QLabel('姓名')
        name_line_edit = QLineEdit('')
        introduction_label = QLabel('简介')
        introduction_line_edit = QTextEdit('')

        form_layout.addRow(name_label, name_line_edit)
        form_layout.addRow(introduction_label, introduction_line_edit)
        self.setLayout(form_layout)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
