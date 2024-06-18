import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QMessageBox

class FoodOrderingSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        # Set window properties
        self.setWindowTitle('Food Ordering System')
        self.setGeometry(100, 100, 400, 300)

        # Create layout
        layout = QVBoxLayout()

        # Create combo box for food selection
        self.food_combo = QComboBox(self)
        self.food_combo.addItem("Nasi Goreng", 20000)
        self.food_combo.addItem("Mie Goreng", 15000)
        self.food_combo.addItem("Ayam Bakar", 25000)
        self.food_combo.addItem("Sate Ayam", 20000)
        self.food_combo.addItem("Bakso", 18000)

        # Create input field for quantity
        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Enter quantity")

        # Create button for adding to order
        self.add_button = QPushButton('Add to Order', self)
        self.add_button.clicked.connect(self.add_to_order)

        # Create label for total price
        self.total_label = QLabel('Total: Rp 0', self)

        # Add widgets to layout
        layout.addWidget(QLabel('Select Food:', self))
        layout.addWidget(self.food_combo)
        layout.addWidget(QLabel('Quantity:', self))
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.total_label)

        # Set layout to the window
        self.setLayout(layout)

        self.total_price = 0

    def add_to_order(self):
        try:
            quantity = int(self.quantity_input.text())
            if quantity <= 0:
                raise ValueError

            # Get selected food price
            food_price = self.food_combo.currentData()

            # Calculate total price
            self.total_price += food_price * quantity

            # Update total label
            self.total_label.setText(f'Total: Rp {self.total_price}')
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid quantity.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FoodOrderingSystem()
    window.show()
    sys.exit(app.exec_())
