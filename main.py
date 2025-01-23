from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout
from PyQt5.QtCore import Qt
import sys

class PyMathCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyMath 1.0")
        self.setFixedSize(360, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_ui()

    def create_ui(self):
        # Display panel
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet(
            "font-size: 24px; height: 60px; background-color: #9D9D9D; border: 1px solid #FF5733; border-radius: 5px; padding: 10px;"
        )
        self.layout.addWidget(self.display)

        # Button layout
        button_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setStyleSheet(
                "font-size: 18px; height: 60px; background-color: #9D9D9D; border: 1px solid #FF5733; border-radius: 5px;"
                "hover { background-color: #d9d9d9; }"
            )
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            button_layout.addWidget(button, row, col)

        self.layout.addLayout(button_layout)

    def on_button_click(self, char):
        if char == "C":
            self.display.clear()
        elif char == "=":
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + char)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = PyMathCalculator()
    calculator.show()
    sys.exit(app.exec_())

