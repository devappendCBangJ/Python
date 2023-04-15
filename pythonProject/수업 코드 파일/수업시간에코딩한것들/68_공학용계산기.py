from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import math
import os

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

ui_file = resource_path("./calculator.ui")

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.equalbutton.clicked.connect(self.calculate)

    def calculate(self):
        equation = self.inputbox.text()
        result = eval(equation)
        history_text = "{}\n= {}\n".format(equation, result)
        self.history.append(history_text)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())