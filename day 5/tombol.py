import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# Fungsi untuk menangani klik tombol
def on_button_clicked():
    print("Tombol ditekan!")

# Kelas untuk membuat jendela utama
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Mengatur judul jendela
        self.setWindowTitle('Aplikasi PyQt Sederhana')

        # Membuat tombol
        self.button = QPushButton('Klik Saya', self)
        self.button.clicked.connect(on_button_clicked)

        # Menambahkan tombol ke dalam layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        
        # Mengatur layout ke dalam jendela
        self.setLayout(layout)

        # Mengatur ukuran jendela
        self.resize(300, 200)

# Fungsi utama untuk menjalankan aplikasi
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
