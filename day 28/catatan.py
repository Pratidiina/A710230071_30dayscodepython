import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class NoteManager(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Note Manager")
        self.setGeometry(100, 100, 500, 400)
        
        self.notes = []
        
        self.initUI()
    
    def initUI(self):
        main_layout = QVBoxLayout()
        
        # Input layout
        input_layout = QHBoxLayout()
        self.note_input = QLineEdit(self)
        self.note_input.setPlaceholderText("Enter your note here...")
        add_button = QPushButton("Add Note", self)
        add_button.clicked.connect(self.add_note)
        
        input_layout.addWidget(self.note_input)
        input_layout.addWidget(add_button)
        
        # Notes list
        self.note_list = QListWidget(self)
        self.note_list.itemDoubleClicked.connect(self.delete_note)
        
        # Main layout
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.note_list)
        
        container = QWidget()
        container.setLayout(main_layout)
        
        self.setCentralWidget(container)
    
    def add_note(self):
        note_text = self.note_input.text()
        if note_text:
            self.notes.append(note_text)
            self.note_list.addItem(note_text)
            self.note_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Note cannot be empty")
    
    def delete_note(self, item):
        reply = QMessageBox.question(self, 'Delete Note', 'Are you sure you want to delete this note?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.notes.remove(item.text())
            self.note_list.takeItem(self.note_list.row(item))

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = NoteManager()
    
    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = App()
    app.run()
