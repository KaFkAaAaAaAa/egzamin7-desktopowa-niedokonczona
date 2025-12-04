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

        self.ui.userNumber.editingFinished.connect(self.editFinish)

        self.ui.blueEye.setChecked(True)

        self.ui.imageLeft.setPixmap(QPixmap("./000-zdjecie.jpg"))
        self.ui.imageRight.setPixmap(QPixmap("./000-odcisk.jpg"))

        self.ui.acceptButton.clicked.connect(self.okButton)

        self.show()

    def editFinish(self):
        number = self.ui.userNumber.text()

        if number == "333":
            zdjecie1L = QPixmap('./333-zdjecie.jpg')
            zdjecie1R = QPixmap('./333-odcisk.jpg')
            self.ui.imageLeft.setPixmap(zdjecie1L)
            self.ui.imageRight.setPixmap(zdjecie1R)
        elif number == "111":
            zdjecie2L = QPixmap('./111-zdjecie.jpg')
            zdjecie2R = QPixmap('./111-odcisk.jpg')
            self.ui.imageLeft.setPixmap(zdjecie2L)
            self.ui.imageRight.setPixmap(zdjecie2R)
        else:
            self.ui.imageLeft.setPixmap(QPixmap(""))
            self.ui.imageRight.setPixmap(QPixmap(""))

    def okButton(self):
        name = self.ui.userName.text()
        surname = self.ui.userSurname.text()

        eye_color = ""

        if self.ui.blueEye.isChecked():
            eye_color = "niebieskie"
        elif self.ui.brownEye.isChecked():
            eye_color = "piwne"
        else:
            eye_color = "zielone"

        if name == "" or surname == "":
            QMessageBox.information(self, "Info", "Wprowadź dane")
        else:
            QMessageBox.information(self, "Info", f"{name} {surname} kolor oczu {eye_color}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = My_Dialog()
    sys.exit(app.exec())