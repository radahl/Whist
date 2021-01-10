# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputNavn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InputNavn(object):
    def setupUi(self, InputNavn):
        InputNavn.setObjectName("InputNavn")
        InputNavn.resize(342, 218)
        self.buttonBox = QtWidgets.QDialogButtonBox(InputNavn)
        self.buttonBox.setGeometry(QtCore.QRect(90, 130, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(InputNavn)
        self.label.setGeometry(QtCore.QRect(70, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(InputNavn)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
#        self.lineEdit.setText("Hej")

        self.retranslateUi(InputNavn)
        self.buttonBox.accepted.connect(lambda: Navn(InputWin = InputNavn, InpuBox = self.lineEdit))
        self.buttonBox.rejected.connect(InputNavn.reject)
        QtCore.QMetaObject.connectSlotsByName(InputNavn)

    def retranslateUi(self, InputNavn):
        _translate = QtCore.QCoreApplication.translate
        InputNavn.setWindowTitle(_translate("InputNavn", "Dialog"))
        self.label.setText(_translate("InputNavn", "Deltager Navn"))


    def run(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_InputNavn()
        ui.setupUi(Dialog)
        Dialog.show()
        ui.lineEdit.setFocus()
        Dialog.exec_()
        return(Dialog.Navn)

def Navn(InputWin, InpuBox):
    InputWin.Navn = InpuBox.text()
    InputWin.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputNavn = QtWidgets.QDialog()
    ui = Ui_InputNavn()
    ui.setupUi(InputNavn)
    InputNavn.show()
    sys.exit(app.exec_())

