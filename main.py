from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtWidgets
from random import randint
from UI import Ui
import sys

app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
ui = Ui()
ui.setupUi(mw)
mw.show()

ui.label.setFixedSize(400, 400)
ui.label.setPixmap(QPixmap(400, 400))
ui.label.move(100, 100)


def circle(self):
    x, y = randint(100, 300), randint(100, 300)
    r = randint(10, 100)
    painter = QPainter(ui.label.pixmap())
    pen = QPen()
    pen.setWidth(3)
    pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
    painter.setPen(pen)
    painter.drawEllipse(x, y, r, r)
    painter.end()
    mw.update()


ui.pushButton.clicked.connect(circle)

sys.exit(app.exec_())
