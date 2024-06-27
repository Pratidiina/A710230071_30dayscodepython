import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Membuat layout utama
        vbox = QVBoxLayout()

        # Membuat dan menambahkan QLineEdit untuk display kalkulator
        self.display = QLineEdit(self)
        vbox.addWidget(self.display)

        # Membuat layout untuk tombol-tombol
        grid_layout = QVBoxLayout()

        # Baris pertama tombol
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QPushButton('7', self))
        hbox1.addWidget(QPushButton('8', self))
        hbox1.addWidget(QPushButton('9', self))
        hbox1.addWidget(QPushButton('/', self))
        grid_layout.addLayout(hbox1)

        # Baris kedua tombol
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QPushButton('4', self))
        hbox2.addWidget(QPushButton('5', self))
        hbox2.addWidget(QPushButton('6', self))
        hbox2.addWidget(QPushButton('*', self))
        grid_layout.addLayout(hbox2)

        # Baris ketiga tombol
        hbox3 = QHBo
