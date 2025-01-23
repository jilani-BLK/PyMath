from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout, QLabel, QTextEdit
from PyQt5.QtCore import Qt
import sys
import math

class PyMathCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyMath 1.0")
        self.setFixedSize(360, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.history = [] 
        self.create_ui()

    def create_ui(self):

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet(
            "font-size: 23px; height: 60px; background-color: #FFFFFF; color: #000000; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
        )
        self.layout.addWidget(self.display)

        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        self.history_display.setStyleSheet(
            "font-size: 20px; height: 15px; background-color: #F7F7F7; color: #000000; border: 1px solid #CCC; border-radius: 8px; padding: 5px;"
        )
        self.layout.addWidget(self.history_display)

        button_layout = QGridLayout()
        buttons = [
            ('C', 0, 0), ('←', 0, 1), ('%', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('√', 4, 1), ('=', 4, 2), ('Supp', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
            ('x^y', 6, 0), ('e^x', 6, 1), ('x!', 6, 2)
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFixedSize(80, 60)
            
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            button_layout.addWidget(button, row, col, 1, 1)

        button_layout.setHorizontalSpacing(10)  
        button_layout.setVerticalSpacing(10)   

        self.layout.addLayout(button_layout)

    def on_button_click(self, char):
        if char == "C":
            self.display.clear()
        elif char == "←":
            self.display.setText(self.display.text()[:-1])
        elif char == "=":
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
                self.history.append(f"{expression} = {result}")
                self.update_history_display()
            except ZeroDivisionError:
                self.display.setText("Cannot divide by zero")
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "%":
            try:
                expression = self.display.text()
                result = eval(expression) / 100
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "√":
            try:
                expression = self.display.text()
                result = math.sqrt(float(expression))
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "x^y":
            try:
                base, exponent = map(float, self.display.text().split('^'))
                result = math.pow(base, exponent)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "e^x":
            try:
                expression = self.display.text()
                result = math.exp(float(expression))
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "x!":
            try:
                expression = self.display.text()
                result = math.factorial(int(expression))
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "History":
            self.history.clear()
            self.update_history_display()
        elif char in {"sin", "cos", "tan", "log"}:
            try:
                expression = self.display.text()
                if char == "sin":
                    result = math.sin(math.radians(float(expression)))
                elif char == "cos":
                    result = math.cos(math.radians(float(expression)))
                elif char == "tan":
                    result = math.tan(math.radians(float(expression)))
                elif char == "log":
                    result = math.log10(float(expression))
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Invalid Input")
        else:
            self.display.setText(self.display.text() + char)

    def update_history_display(self):
        self.history_display.setText("\n".join(self.history))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = PyMathCalculator()
    calculator.show()
    sys.exit(app.exec_())
