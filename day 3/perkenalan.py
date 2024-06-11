import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class Perkenalan(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Layout
        layout = QVBoxLayout()
        
        # Label dan Input untuk Nama
        self.nameLabel = QLabel("Nama:", self)
        self.nameInput = QLineEdit(self)
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.nameInput)
        
        # Label dan Input untuk NIM
        self.nimLabel = QLabel("NIM:", self)
        self.nimInput = QLineEdit(self)
        layout.addWidget(self.nimLabel)
        layout.addWidget(self.nimInput)
        
        # Tombol Submit
        self.submitButton = QPushButton("Submit", self)
        self.submitButton.clicked.connect(self.onSubmit)
        layout.addWidget(self.submitButton)
        
        # Set Layout ke Window
        self.setLayout(layout)
        
        # Konfigurasi Window
        self.setWindowTitle("Perkenalan Nama dan NIM")
        self.setGeometry(100, 100, 300, 200)
        
    def onSubmit(self):
        nama = self.nameInput.text()
        nim = self.nimInput.text()
        
        # Menampilkan informasi menggunakan QMessageBox
        QMessageBox.information(self, "Informasi", f"Nama: {nama}\nNIM: {nim}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    perkenalan = Perkenalan()
    perkenalan.show()
    sys.exit(app.exec_())
