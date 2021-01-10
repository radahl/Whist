# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:54:12 2021

@author: radah
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from WhistMainWindow import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
