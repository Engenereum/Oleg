import random

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MyWindow(QMainWindow):
    def __init__(self, speed_x, speed_y):
        super().__init__()
        self.window_speed_x = speed_x
        self.window_speed_y = speed_y
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setFixedSize(200, 200)
        self.move(random.randint(0, 1920), random.randint(0, 1080))
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_func)
        self.timer.start(10)
        #pixmap = QPixmap()
        #pixmap.load("сбк2.png")
        #pixmap = pixmap.scaled(200, 200)

        label = QLabel(self)
        #label.setPixmap(pixmap)
        label.setFixedSize(200, 200)
        self.show()

    def timer_func(self):
        w = self.width()
        h = self.height()
        x = self.x()
        y = self.y()

        if self.window_speed_x > 0 and x + w + self.window_speed_x >= 1920:
            self.window_speed_x = -self.window_speed_x
        if self.window_speed_x < 0 and x + self.window_speed_x <= 0:
            self.window_speed_x = -self.window_speed_x
        if self.window_speed_y > 0 and y + h + self.window_speed_y >= 1080:
            self.window_speed_y = -self.window_speed_y
        if self.window_speed_y < 0 and y + self.window_speed_x <= 0:
            self.window_speed_y = -self.window_speed_y

        self.move(x + self.window_speed_x, y + self.window_speed_y)


if __name__ == "__main__":
    app = QApplication([])
    wnd = []
    for i in range(10):
        wnd.append(MyWindow(random.randint(0,20), random.randint(0,20)))
    app.exec()
