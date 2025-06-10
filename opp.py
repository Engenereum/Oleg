from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 300)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.button = QPushButton(self)
        self.setMouseTracking(False)
        self.offset = None
        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        x = self.button.x()
        y = self.button.y()
        window_x = self.x()
        window_y = self.y()
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
        if x + dx + self.button.width() > self.width():
            self.move(window_x + dx, window_y)
        elif x + dx < 0:
            self.move(window_x + dx, window_y)
        elif y + dy + self.button.height() > self.height():
            self.move(window_x, window_y + dy)
        elif y + dy < 0:
            self.move(window_x, window_y + dy)
        else:
            self.button.move(x + dx, y + dy)
        print(f"Нажата кнопка {key}")

    def keyReleaseEvent(self, event):
        print("Кнопка отпущена")

    def mouseReleaseEvent(self, event):
        print("Отпущена конпка")

    def mousePressEvent(self, event):
        event: QMouseEvent
        self.offset = event.pos()
        print("Нажата кнопка")

    def mouseDoubleClickEvent(self, event):
        print("Двойное нажатие")

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        dx = self.offset.x()
        dy = self.offset.y()
        self.move(x + dx, y + dy)


if __name__ == "__main__":
    app = QApplication([])
    wnd = MyWindow()

    app.exec()
