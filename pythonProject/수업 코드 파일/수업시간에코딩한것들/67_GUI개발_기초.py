from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os

ui_file = "./test.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.pushButton.clicked.connect(self.buttonCilcked)

    def buttonCilcked(self):
        result = self.lineEdit.text()
        self.label.setText(result)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())