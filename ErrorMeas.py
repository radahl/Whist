# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 13:19:55 2021

@author: radah
"""

from PyQt5 import QtWidgets

def ShowErr(tex):
    error_dialog = QtWidgets.QErrorMessage()
    error_dialog.setEnabled(True)
    error_dialog.showMessage(tex)
    error_dialog.exec_()
    
#ShowErr(tex)