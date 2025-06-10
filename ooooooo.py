import random

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


def sbk():
    window = QMainWindow()
    window.setFixedSize(1100, 200)
    pixmap = QPixmap()
    pixmap.load("сбк2.png")
    pixmap = pixmap.scaled(1100, 200)
    label = QLabel(window)
    label.setPixmap(pixmap)
    label.setFixedSize(1100, 200)
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    window.move(x, y)
    window.show()
    return window


app = QApplication([])
window = QMainWindow()

window.setFixedSize(1100, 200)

pixmap = QPixmap()
pixmap.load("сбк2.png")
pixmap = pixmap.scaled(1100, 200)

label = QLabel(window)
label.setPixmap(pixmap)
label.setFixedSize(1100, 200)

window.show()

window2 = QMainWindow()

window2.setFixedSize(1100, 200)

pixmap2 = QPixmap()
pixmap2.load("сбк2.png")
pixmap2 = pixmap2.scaled(1100, 200)

label = QLabel(window2)
label.setPixmap(pixmap2)
label.setFixedSize(1100, 200)

window2.show()

window3 = QMainWindow()

window3.setFixedSize(1100, 200)

pixmap3 = QPixmap()
pixmap3.load("сбк2.png")
pixmap3 = pixmap3.scaled(1100, 200)

label = QLabel(window3)
label.setPixmap(pixmap3)
label.setFixedSize(1100, 200)

label2 = QLabel(window3)
font = QFont("times", 300)
label2.setFont(font)
label2.setFixedSize(1100, 200)
label2.setText("Лох")

window3.show()

window4 = QMainWindow()

window4.setFixedSize(1100, 200)

pixmap4 = QPixmap()
pixmap4.load("сбк2.png")
pixmap4 = pixmap4.scaled(1100, 200)

label = QLabel(window4)
label.setPixmap(pixmap4)
label.setFixedSize(1100, 200)

label3 = QLabel(window4)
font = QFont("times", 300)
label3.setFont(font)
label3.setFixedSize(1100, 200)
label3.setText("сбк")

window4.show()
win = []
for i in range(9):
    win.append(sbk())

app.exec()
