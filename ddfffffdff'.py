import random

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtWidgets import QApplication

from grafics import MyWindow


class MyWidowRewrited(MyWindow):
    def __init__(self):
        super().__init__(5, 5)
        self.timer.stop()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_func)
        self.is_need_to_draw_window = True
        self.timer.start(100)
    
    def timer_func(self):
        self.is_need_to_draw_window = not self.is_need_to_draw_window
        self.update()
    def keyPressEvent(self, event):
        key = event.key()
        x = self.x()
        y = self.y()
        dx = 0
        dy = 0
        if key == Qt.Key_W:
            dy = -5
        elif key == Qt.Key_S:
            dy = 5
        elif key == Qt.Key_A:
            dx = -5
        elif key == Qt.Key_D:
            dx = 5
        if x + dx + self.width() > 1920:
            self.move(x + dx, y)
        elif x + dx < 0:
            self.move(x + dx, y)
        elif y + dy + self.height() > 1080:
            self.move(x, y + dy)
        elif y + dy < 0:
            self.move(x, y + dy)
        else:
            self.move(x + dx, y + dy)

    def paintEvent(self, event):
        if self.is_need_to_draw_window:
            painter = QPainter(self)
            pen = QPen()
            pen.setWidth(22)
            pen.setColor(QColor(225, 0, 0))
            painter.setPen(pen)
            brush = QBrush()
            brush.setColor(QColor(0, 255, 0))
            brush.setStyle(Qt.HorPattern)
            painter.setBrush(brush)
            painter.drawRect(0,0, self.width(), self.height())
            painter.drawLine(0, 0, self.width(), self.height())
            painter.drawLine(self.width(), 0, 0, self.height())


if __name__ == "__main__":
    app = QApplication([])
    wnd = []
    for i in range(10):
        wnd.append(MyWindow(random.randint(0, 20), random.randint(0, 20)))
    wnd2 = MyWidowRewrited()
    app.exec()
