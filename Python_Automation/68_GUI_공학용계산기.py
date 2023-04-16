# <파이썬 계산 함수>
    # 파이썬 제공 계산 함수 : eval("계산식")
        # - 계산식 예시 : 2 * 3, 2 ** 3, 2 % 3 등등 파이썬에서 사용하는 수식 전부

from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import math

ui_file = "./GUI/calculator.ui"

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.calbutton.clicked.connect(self.calculate)

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