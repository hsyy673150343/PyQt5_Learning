# -*- coding:utf8 -*-
# @TIME     :2019/5/12 18:11
# @Author   : 洪松
# @File     : test_7.py

import sys
from PyQt5.QtWidgets import QWidget, QLCDNumber, QDial, QApplication, QSlider


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        lcd = QLCDNumber(self)
        # dial = QDial(self)
        dial = QSlider(self)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('简单的信号与槽示例')

        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)

        dial.valueChanged.connect(lcd.display)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())