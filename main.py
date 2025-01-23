from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout, QLabel, QTextEdit, QMenuBar, QAction, QFileDialog
from PyQt5.QtCore import Qt
import sys
import math
from fractions import Fraction

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
        self.memory = 0  
        self.create_menu()
        self.create_ui()

    def create_menu(self):
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        file_menu = menubar.addMenu("File")

        save_action = QAction("Save History", self)
        save_action.triggered.connect(self.save_history_to_file)
        file_menu.addAction(save_action)

        clear_memory_action = QAction("Clear Memory", self)
        clear_memory_action.triggered.connect(self.clear_memory)
        file_menu.addAction(clear_memory_action)

    def create_ui(self):
        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet(
            "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #A9A9A9; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
        )
        self.layout.addWidget(self.display)

        self.history_display = QTextEdit("Historique")
        self.history_display.setReadOnly(True)
        self.history_display.setStyleSheet(
            "font-size: 16px; height: 15px; background-color: #F7F7F7; color: #A9A9A9; border: 1px solid #CCC; border-radius: 8px; padding: 5px;"
        )
        self.layout.addWidget(self.history_display)

        button_layout = QGridLayout()
        buttons = [
            ('C', 0, 0), ('←', 0, 1), ('%', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('√', 4, 1), ('=', 4, 2), ('History', 4, 3),
            ('M+', 5, 0), ('MR', 5, 1), ('MC', 5, 2), ('Fraction', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFixedSize(80, 60)
            
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            button_layout.addWidget(button, row, col, 1, 1)

        button_layout.setHorizontalSpacing(10)  
        button_layout.setVerticalSpacing(10)    

        self.layout.addLayout(button_layout)

    def save_history_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save History", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "w") as file:
                file.write("\n".join(self.history))

    def clear_memory(self):
        self.memory = 0

    def on_button_click(self, char):
        if char == "C":
            self.display.clear()
            self.display.setText("0")
            self.display.setStyleSheet(
                "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #A9A9A9; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
            )
        elif char == "←":
            text = self.display.text()
            if len(text) > 1:
                self.display.setText(text[:-1])
            else:
                self.display.setText("0")
                self.display.setStyleSheet(
                    "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #A9A9A9; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
                )
        elif char == "=":
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
                self.display.setStyleSheet(
                    "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #000000; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
                )
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
                self.display.setStyleSheet(
                    "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #000000; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
                )
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "√":
            try:
                expression = self.display.text()
                result = math.sqrt(float(expression))
                self.display.setText(str(result))
                self.display.setStyleSheet(
                    "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #000000; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
                )
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "Fraction":
            try:
                expression = self.display.text()
                result = Fraction(expression)
                self.display.setText(str(result))
                self.display.setStyleSheet(
                    "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #000000; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
                )
            except Exception:
                self.display.setText("Invalid Fraction")
        elif char == "M+":
            try:
                self.memory += float(self.display.text())
            except Exception:
                self.display.setText("Invalid Input")
        elif char == "MR":
            self.display.setText(str(self.memory))
            self.display.setStyleSheet(
                "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #000000; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
            )
        elif char == "MC":
            self.memory = 0
        elif char == "History":
            self.history.clear()
            self.update_history_display()
        else:
            if self.display.text() == "0":
                self.display.setText(char)
            else:
                self.display.setText(self.display.text() + char)
            self.display.setStyleSheet(
                "font-size: 23px; height: 60px; background-color: #F7F7F7; color: #000000; border: 2px solid #CCC; border-radius: 8px; padding: 10px;"
            )

    def update_history_display(self):
        self.history_display.setText("\n".join(self.history))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = PyMathCalculator()
    calculator.show()
    sys.exit(app.exec_())
