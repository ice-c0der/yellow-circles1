import sys
import random
from UI import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

class Prog(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        self.draw_now = 0

    def draw(self, qp):
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        a = random.randint(100, 300)
        qp.drawEllipse(10, 10, a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = Prog()
    prog.show()
    sys.exit(app.exec())
