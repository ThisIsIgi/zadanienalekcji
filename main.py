import sys
import re
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class Myform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.save.clicked.connect(self.function)
        self.ui.savetofile.clicked.connect(self.functiontwo)


    def function(self):
        pesel = self.ui.pesel.text()


        if (re.match('[0-9]{11}$', pesel)):
            pass
        else:
            messagebox = QMessageBox()
            messagebox.setInformativeText("Bledny pesel")
            messagebox.setStandardButtons(QMessageBox.StandardButton.Ok)
            messagebox.setWindowTitle("Komunikat")
            messagebox.exec()

        l = int(pesel[10])
        suma = ((l * int(pesel[0])) + (3 * int(pesel[l])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + (
        (l * int(pesel[4]))) + (3 * int(pesel[5])) + (7 * int(pesel[6])) + (9 * int(pesel[7])) + (l * int(pesel[8])) + (3 * int(pesel[9])))
        kontrolka = 10 - (suma % 10)

        if kontrolka == 10:
            kontrolka = 0
        else:
            kontrolka = kontrolka

        if ((kontrolka == 10) or (kontrolka == 0)):
            imie = self.ui.name.text()
            nazwisko = self.ui.surname.text()
            self.ui.listWidget.addItem(f"{imie} {nazwisko}")
        else:
            messagebox = QMessageBox()
            messagebox.setInformativeText("Bledny pesel")
            messagebox.setStandardButtons(QMessageBox.StandardButton.Ok)
            messagebox.setWindowTitle("Komunikat")
            messagebox.exec()

    def functiontwo(self):
        pesel = self.ui.pesel.text()
        if re.match('[0-9]{11}$', pesel):
            pass
        else:
            messagebox = QMessageBox()
            messagebox.setInformativeText("Bledny pesel")
            messagebox.setStandardButtons(QMessageBox.StandardButton.Ok)
            messagebox.setWindowTitle("Komunikat")
            messagebox.exec()

        l = int(pesel[10])
        suma = ((l * int(pesel[0])) + (3 * int(pesel[l])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + (
        (l * int(pesel[4]))) + (3 * int(pesel[5])) + (7 * int(pesel[6])) + (9 * int(pesel[7])) + (l * int(pesel[8])) + (3 * int(pesel[9])))
        kontrolka = 10 - (suma % 10)

        if kontrolka == 10:
            kontrolka = 0
        else:
            kontrolka = kontrolka

        if ((kontrolka == 10) or (kontrolka == 0)):
            imie = self.ui.name.text()
            nazwisko = self.ui.surname.text()
            tel = self.ui.phone.text()
            plik = 'imie_nazwisko.txt'
            with open(plik, "a")as plik:
                plik.write(f"imie: {imie}, nazwisko: {nazwisko}, telefon: {tel}")
                messagebox = QMessageBox()
                messagebox.setInformativeText("zapisano")
                messagebox.setStandardButtons(QMessageBox.StandardButton.Ok)
                messagebox.setWindowTitle("Komunikat")
                messagebox.exec()


        else:
            messagebox = QMessageBox()
            messagebox.setInformativeText("Bledny pesel")
            messagebox.setStandardButtons(QMessageBox.StandardButton.Ok)
            messagebox.setWindowTitle("Komunikat")
            messagebox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())