import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter


def rand():
    return random.randint(100, 300)


class RandCircle(QMainWindow):
    def __init__(self):
        super(RandCircle, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            pai = QPainter(self)
            pai.begin(self)
            self.painter(pai)
            pai.end()

    def painter(self, pai):
        n = 0
        pai.setBrush(QColor(255, 255, 0))
        m = rand()
        n = rand()
        pai.drawEllipse(m, n, m // 4, m // 4)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rc = RandCircle()
    rc.show()
    sys.exit(app.exec())