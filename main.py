from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from sys import argv, exit
from random import choice


class CyrcleVashka(QWidget):
    def __init__(self):
        uic.loadUi('disg.ui', self)
        super().__init__()
        self.setup()

    def setup(self):
        pass


if __name__ == '__main__':
    app = QApplication(argv)
    ex = CyrcleVashka()
    ex.show()
    exit(app.exec())