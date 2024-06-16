import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTimeEdit, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Timer App')

        self.layout = QVBoxLayout()

        self.time_display = QLabel('00:00:00', self)
        self.time_display.setStyleSheet("font-size: 30px;")
        self.layout.addWidget(self.time_display)

        self.time_input = QTimeEdit(self)
        self.time_input.setDisplayFormat('HH:mm:ss')
        self.layout.addWidget(self.time_input)

        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.stop_button)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_timer)
        self.layout.addWidget(self.reset_button)

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_left = QTime(0, 0, 0)

    def start_timer(self):
        self.time_left = self.time_input.time()
        self.update_display()
        self.timer.start(1000)  # Update every second

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.time_left = QTime(0, 0, 0)
        self.update_display()

    def update_timer(self):
        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()
        else:
            self.time_left = self.time_left.addSecs(-1)
            self.update_display()

    def update_display(self):
        self.time_display.setText(self.time_left.toString('HH:mm:ss'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerApp()
    ex.show()
    sys.exit(app.exec_())
