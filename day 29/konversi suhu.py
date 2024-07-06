import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

class TemperatureConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set judul jendela
        self.setWindowTitle("Temperature Converter")

        # Set ukuran jendela
        self.setGeometry(100, 100, 300, 150)

        # Buat widget utama
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Buat layout vertikal
        self.layout = QVBoxLayout()

        # Buat input untuk suhu
        self.input_temp = QLineEdit(self)
        self.input_temp.setPlaceholderText("Masukkan suhu")
        self.layout.addWidget(self.input_temp)

        # Buat tombol untuk konversi Celsius ke Fahrenheit
        self.btn_c_to_f = QPushButton("Celsius ke Fahrenheit", self)
        self.btn_c_to_f.clicked.connect(self.convert_c_to_f)
        self.layout.addWidget(self.btn_c_to_f)

        # Buat tombol untuk konversi Fahrenheit ke Celsius
        self.btn_f_to_c = QPushButton("Fahrenheit ke Celsius", self)
        self.btn_f_to_c.clicked.connect(self.convert_f_to_c)
        self.layout.addWidget(self.btn_f_to_c)

        # Buat label untuk menampilkan hasil
        self.result_label = QLabel("Hasil konversi akan muncul di sini", self)
        self.layout.addWidget(self.result_label)

        # Set layout ke widget utama
        self.central_widget.setLayout(self.layout)

    def convert_c_to_f(self):
        try:
            celsius = float(self.input_temp.text())
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.setText(f"{celsius}°C = {fahrenheit}°F")
        except ValueError:
            self.result_label.setText("Input tidak valid. Masukkan angka.")

    def convert_f_to_c(self):
        try:
            fahrenheit = float(self.input_temp.text())
            celsius = (fahrenheit - 32) * 5/9
            self.result_label.setText(f"{fahrenheit}°F = {celsius}°C")
        except ValueError:
            self.result_label.setText("Input tidak valid. Masukkan angka.")

def main():
    app = QApplication(sys.argv)
    window = TemperatureConverter()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
