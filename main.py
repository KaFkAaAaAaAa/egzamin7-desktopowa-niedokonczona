import sys
from tkinter import Image

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class My_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.blueEye.setChecked(True)

        self.ui.acceptButton.clicked.connect(self.okButton)

        self.show()


    def okButton(self):
        if self.ui.userNumber == "333":
            pixmap = QPixmap("./333-zdjecie.jpg")
            self.ui.imageLeft.setPixmap("./333-zdjecie.jpg")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = My_Dialog()
    sys.exit(app.exec())