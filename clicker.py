import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

cc = 0
r = 0


def func():
    global cc
    cc += 1
    label.setText(str(cc))


def func2():
    print("Прппрпрпп")


def timer_func():
    print("ЪХ")
    global cc
    global r
    if cc > r:
        r = cc
    cc = 0
    label2.setText(f"Рекорд: {r}")


def timer_func2():
    now = datetime.datetime.now()
    label3.setText(f"Время {now}")


app = QApplication([])
window = QMainWindow()

window.setWindowTitle("Лох")
window.setFixedSize(800, 800)
window.setCursor(QtCore.Qt.WaitCursor)
window.setWindowOpacity(1)

button = QPushButton(window)
button.setFixedSize(200, 200)
button.setText("Лох")
button.clicked.connect(func)
button.clicked.connect(func2)
button.move(300, 100)

timer = QTimer()
timer.timeout.connect(timer_func)
timer.start(2147483647)

timer2 = QTimer()
timer2.timeout.connect(timer_func2)
timer2.start(1000)

label = QLabel(window)
label.setText("Лох2")

label2 = QLabel(window)
label2.setFixedSize(200, 20)
label2.move(0, 40)

label3 = QLabel(window)
label3.setFixedSize(200, 20)
label3.move(0, 80)

window.show()
app.exec()
