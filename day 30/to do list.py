import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

# Kelas Tugas
class Tugas:
    def __init__(self, deskripsi, prioritas):
        self.deskripsi = deskripsi
        self.prioritas = prioritas

    def __str__(self):
        return f"{self.deskripsi} (Prioritas: {self.prioritas})"

# Kelas Manajemen Tugas
class ManajemenTugas:
    def __init__(self):
        self.daftar_tugas = []

    def tambah_tugas(self, tugas):
        self.daftar_tugas.append(tugas)

    def hapus_tugas(self, index):
        if 0 <= index < len(self.daftar_tugas):
            del self.daftar_tugas[index]

    def tampilkan_tugas(self):
        for i, tugas in enumerate(self.daftar_tugas):
            print(f"{i + 1}. {tugas}")

# Antarmuka PyQt5
class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.manajemen_tugas = ManajemenTugas()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi To-Do List')

        self.layout = QVBoxLayout()

        self.deskripsi_label = QLabel('Deskripsi Tugas:')
        self.layout.addWidget(self.deskripsi_label)

        self.deskripsi_input = QLineEdit(self)
        self.layout.addWidget(self.deskripsi_input)

        self.prioritas_label = QLabel('Prioritas Tugas:')
        self.layout.addWidget(self.prioritas_label)

        self.prioritas_input = QLineEdit(self)
        self.layout.addWidget(self.prioritas_input)

        self.tambah_button = QPushButton('Tambah Tugas', self)
        self.tambah_button.clicked.connect(self.tambah_tugas)
        self.layout.addWidget(self.tambah_button)

        self.list_widget = QListWidget(self)
        self.layout.addWidget(self.list_widget)

        self.hapus_button = QPushButton('Hapus Tugas', self)
        self.hapus_button.clicked.connect(self.hapus_tugas)
        self.layout.addWidget(self.hapus_button)

        self.setLayout(self.layout)
        self.show()

    def tambah_tugas(self):
        deskripsi = self.deskripsi_input.text()
        prioritas = self.prioritas_input.text()

        if deskripsi and prioritas:
            tugas = Tugas(deskripsi, prioritas)
            self.manajemen_tugas.tambah_tugas(tugas)
            self.list_widget.addItem(str(tugas))
            self.deskripsi_input.clear()
            self.prioritas_input.clear()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Deskripsi dan Prioritas tidak boleh kosong.')

    def hapus_tugas(self):
        selected_item = self.list_widget.currentRow()
        if selected_item >= 0:
            self.manajemen_tugas.hapus_tugas(selected_item)
            self.list_widget.takeItem(selected_item)
        else:
            QMessageBox.warning(self, 'Peringatan', 'Pilih tugas yang ingin dihapus.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToDoApp()
    sys.exit(app.exec_())
