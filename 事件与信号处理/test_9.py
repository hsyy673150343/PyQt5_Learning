# -*- coding:utf8 -*-
# @TIME     :2019/5/12 20:48
# @Author   : 洪松
# @File     : test_9.py

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPainter


class Example(QWidget):
    distance_from_center = 0

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('重写鼠标事件和绘图事件')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, QMouseEvent):
        distance_from_center = round(((QMouseEvent.y() - 250)**2 + (QMouseEvent.x() - 500)**2)**0.5)
        self.label.setText('坐标: ( x: %d ,y: %d )' % (QMouseEvent.x(),\
                                                     QMouseEvent.y()) + " 离中心点距离: " + str(distance_from_center))
        self.pos = QMouseEvent.pos()
        self.update()

    def paintEvent(self, QPaintEvent):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())