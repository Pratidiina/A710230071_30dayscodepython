import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QListWidget, QMessageBox, QInputDialog


class NoteManager(QWidget):
    def __init__(self):
        super().__init__()

        self.notes = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Note Manager')

        layout = QVBoxLayout()

        self.noteList = QListWidget()
        self.noteList.itemClicked.connect(self.displayNote)
        layout.addWidget(self.noteList)

        self.noteContent = QTextEdit()
        layout.addWidget(self.noteContent)

        self.newButton = QPushButton('New Note')
        self.newButton.clicked.connect(self.newNote)
        layout.addWidget(self.newButton)

        self.saveButton = QPushButton('Save Note')
        self.saveButton.clicked.connect(self.saveNote)
        layout.addWidget(self.saveButton)

        self.deleteButton = QPushButton('Delete Note')
        self.deleteButton.clicked.connect(self.deleteNote)
        layout.addWidget(self.deleteButton)

        self.setLayout(layout)

    def newNote(self):
        text, ok = QInputDialog.getText(self, 'New Note', 'Enter note title:')
        if ok and text:
            self.notes[text] = ''
            self.noteList.addItem(text)

    def saveNote(self):
        currentItem = self.noteList.currentItem()
        if currentItem:
            title = currentItem.text()
            self.notes[title] = self.noteContent.toPlainText()
            QMessageBox.information(self, 'Save Note', 'Note saved successfully!')

    def displayNote(self, item):
        title = item.text()
        self.noteContent.setText(self.notes[title])

    def deleteNote(self):
        currentItem = self.noteList.currentItem()
        if currentItem:
            title = currentItem.text()
            del self.notes[title]
            self.noteList.takeItem(self.noteList.row(currentItem))
            self.noteContent.clear()
            QMessageBox.information(self, 'Delete Note', 'Note deleted successfully!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteManager()
    ex.show()
    sys.exit(app.exec_())
