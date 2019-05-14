# -*- coding:utf8 -*-
# @TIME     :2019/5/12 13:50
# @Author   : 洪松
# @File     : test_1.py

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class SigSlot(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('XXOO')
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)

        slider.valueChanged.connect(lcd.display)
        self.resize(350,250)

app = QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())