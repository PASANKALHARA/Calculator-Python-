import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QPushButton, 
                           QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout, 
                           QLabel, QFrame)
from PyQt5.QtCore import Qt
from math import sin, cos, tan, log, log10, sqrt, factorial, exp, pi, e, radians, degrees, pow

class ScientificCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.first_operand = None
        self.operation = None
        self.new_number = True
        self.memory_value = 0
        self.angle_mode = "DEG"
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 400, 600)
        
        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Top bar with menu and title
        top_bar = QHBoxLayout()
        menu_btn = QPushButton("≡")
        menu_btn.setFixedWidth(40)
        title = QLabel("Scientific")
        
        top_bar.addWidget(menu_btn)
        top_bar.addWidget(title)
        top_bar.addStretch()
        
        history_btn = QPushButton("History")
        memory_btn = QPushButton("Memory")
        top_bar.addWidget(history_btn)
        top_bar.addWidget(memory_btn)
        
        top_widget = QWidget()
        top_widget.setLayout(top_bar)
        main_layout.addWidget(top_widget)
        
        # Display field
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("font-size: 40px; padding: 10px;")
        main_layout.addWidget(self.display)
        
        # Memory and mode buttons
        mode_layout = QHBoxLayout()
        mode_buttons = ["DEG", "F-E", "MC", "MR", "M+", "M-", "MS"]
        for text in mode_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            mode_layout.addWidget(btn)
        
        mode_widget = QWidget()
        mode_widget.setLayout(mode_layout)
        main_layout.addWidget(mode_widget)
        
        # Function type selection
        func_layout = QHBoxLayout()
        trig_btn = QPushButton("Trigonometry")
        func_btn = QPushButton("Function")
        func_layout.addWidget(trig_btn)
        func_layout.addWidget(func_btn)
        func_layout.addStretch()
        
        func_widget = QWidget()
        func_widget.setLayout(func_layout)
        main_layout.addWidget(func_widget)
        
        # Calculator buttons
        button_layout = QGridLayout()
        buttons = [
            ["2ⁿᵈ", "π", "e", "C", "⌫"],
            ["x²", "1/x", "|x|", "exp", "mod"],
            ["²√x", "(", ")", "n!", "÷"],
            ["xʸ", "7", "8", "9", "×"],
            ["10ˣ", "4", "5", "6", "−"],
            ["log", "1", "2", "3", "+"],
            ["ln", "+/-", "0", ".", "="]
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                button = QPushButton(text)
                button.setFixedSize(70, 50)
                
                if text == "=":
                    button.setStyleSheet("background-color: #c41e3a; color: white;")
                elif text.isdigit():
                    button.setStyleSheet("background-color: #ffffff;")
                else:
                    button.setStyleSheet("background-color: #f0f0f0;")
                    
                button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
                button_layout.addWidget(button, i, j)
        
        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        main_layout.addWidget(button_widget)

    def on_button_click(self, value):
        current = self.display.text()
        
        if value.isdigit() or value == ".":
            if self.new_number:
                self.display.setText(value)
                self.new_number = False
            else:
                if value == "." and "." in current:
                    return
                self.display.setText(current + value)
        
        elif value in ["π", "e"]:
            self.display.setText(str(pi if value == "π" else e))
            self.new_number = True
        
        elif value == "C":
            self.display.setText("0")
            self.first_operand = None
            self.operation = None
            self.new_number = True
        
        elif value == "⌫":
            if len(current) > 1:
                self.display.setText(current[:-1])
            else:
                self.display.setText("0")
                self.new_number = True
        
        elif value == "+/-":
            if current != "0":
                if current[0] == "-":
                    self.display.setText(current[1:])
                else:
                    self.display.setText("-" + current)
        
        elif value in ["+", "−", "×", "÷", "mod", "xʸ"]:
            try:
                self.first_operand = float(current)
                self.operation = value
                self.new_number = True
            except ValueError:
                QMessageBox.critical(self, "Error", "Invalid input")
        
        elif value == "=":
            try:
                if self.first_operand is not None and self.operation:
                    second_operand = float(current)
                    if self.operation == "+":
                        result = self.first_operand + second_operand
                    elif self.operation == "−":
                        result = self.first_operand - second_operand
                    elif self.operation == "×":
                        result = self.first_operand * second_operand
                    elif self.operation == "÷":
                        if second_operand == 0:
                            raise ValueError("Cannot divide by zero")
                        result = self.first_operand / second_operand
                    elif self.operation == "mod":
                        if second_operand == 0:
                            raise ValueError("Cannot mod by zero")
                        result = self.first_operand % second_operand
                    elif self.operation == "xʸ":
                        result = pow(self.first_operand, second_operand)
                        
                    self.display.setText(str(result))
                    self.first_operand = None
                    self.operation = None
                    self.new_number = True
            except ValueError as e:
                QMessageBox.critical(self, "Error", str(e))
            except Exception as e:
                QMessageBox.critical(self, "Error", "Invalid operation")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = ScientificCalculator()
    calc.show()
    sys.exit(app.exec_())
