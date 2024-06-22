import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QWidget

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 300, 300)

        # Initialize UI elements
        self.initUI()

    def initUI(self):
        # Create the main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        vbox = QVBoxLayout()

        # Create display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(35)
        vbox.addWidget(self.display)

        # Create buttons layout
        buttons_layout = QVBoxLayout()
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        # Create and add buttons to layout
        for row in buttons:
            hbox = QHBoxLayout()
            for btn_text in row:
                button = QPushButton(btn_text)
                button.clicked.connect(self.on_button_click)
                hbox.addWidget(button)
            buttons_layout.addLayout(hbox)

        vbox.addLayout(buttons_layout)
        main_widget.setLayout(vbox)

    def on_button_click(self):
        button_text = self.sender().text()

        if button_text == '=':
            # Evaluate the expression in the display
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        else:
            # Add the clicked button's text to the display
            current_text = self.display.text()
            new_text = current_text + button_text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
