import sys
from random import randint

from ui import Ui_Form
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def circle(self, qp):
        d = randint(0, 300)
        x = randint(100, 150)
        y = randint(100, 150)
        a, b, c = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(a, b, c))
        qp.setPen(QColor(a, b, c))
        qp.drawEllipse(x, y, x + d, y + d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
