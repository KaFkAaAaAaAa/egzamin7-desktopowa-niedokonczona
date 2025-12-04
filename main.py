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
        name = self.ui.userName.toPlainText()
        surname = self.ui.userSurname.toPlainText()
        number = self.ui.userNumber.toPlainText()
        eye_color = ""

        if number == "333":
            pixmap = QPixmap('./333-zdjecie.jpg')
            pixmap1 = QPixmap('./333-odcisk.jpg')
            self.ui.imageLeft.setPixmap(pixmap)
            self.ui.imageRight.setPixmap(pixmap1)
        elif number == "111":
            pixmap2 = QPixmap('./111-zdjecie.jpg')
            self.ui.imageLeft.setPixmap(pixmap2)

        if self.ui.blueEye.isChecked():
            eye_color = "niebieskie"
        elif self.ui.brownEye.isChecked():
            eye_color = "piwne"
        else:
            eye_color = "zielone"

        if name == "" or surname == "" or number == "":
            QMessageBox.information(self, "Info", "Uzupełnij wszystkie pola!")
        else:
            QMessageBox.information(self, "Info", f"{name} {surname} kolor oczu {eye_color}")






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = My_Dialog()
    sys.exit(app.exec())