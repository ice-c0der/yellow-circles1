import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

class Prog(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.But1.clicked.connect(self.paint)
        self.resize(1000, 1000)
        self.draw_now = 0

    def paintEvent(self, event):
        if(not self.draw_now):
            return
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def paint(self):
        self.draw_now = 1
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(255,255,0))
        a = random.randint(100, 300)
        qp.drawEllipse(10, 10, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Prog()
    prog.show()
    sys.exit(app.exec())