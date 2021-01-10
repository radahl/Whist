# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WhistMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
# Begin SECTION setting up the Mainwindow
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1031, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.BeregnScore = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BeregnScore.setObjectName("BeregnScore")
        self.gridLayout.addWidget(self.BeregnScore, 0, 1, 1, 1)
        
        self.ResultatAntalStik = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.ResultatAntalStik.setObjectName("ResultatAntalStik")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.ResultatAntalStik.addItem("")
        self.gridLayout.addWidget(self.ResultatAntalStik, 4, 1, 1, 1)
        
        self.TypeMelding = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TypeMelding.setObjectName("TypeMelding")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.TypeMelding.addItem("")
        self.gridLayout.addWidget(self.TypeMelding, 3, 1, 1, 1)
        
        self.StikMelding = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.StikMelding.setObjectName("StikMelding")
        self.StikMelding.addItem("")
        self.StikMelding.addItem("")
        self.StikMelding.addItem("")
        self.StikMelding.addItem("")
        self.StikMelding.addItem("")
        self.StikMelding.addItem("")
        self.StikMelding.addItem("")
        self.gridLayout.addWidget(self.StikMelding, 2, 1, 1, 1)
        
        self.Score = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.Score.setFrameShape(QtWidgets.QFrame.Panel)
        self.Score.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Score.setLineWidth(2)
        self.Score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Score.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Score.resize(1000, 500)
        self.Score.setWordWrap(False)
        self.Score.setObjectName("Score")
        self.Score.setColumnCount(4)
        self.Score.setRowCount(1)

        item = QtWidgets.QTableWidgetItem()
        self.Score.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Score.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Score.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Score.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Score.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.Score.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.Score.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.Score.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.Score.setItem(0, 3, item)

        self.gridLayout.addWidget(self.Score, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAntal_Spillere = QtWidgets.QAction(MainWindow)
        self.actionAntal_Spillere.setObjectName("actionAntal_Spillere")
        self.actionNyt_Spil = QtWidgets.QAction(MainWindow)
        self.actionNyt_Spil.setObjectName("actionNyt_Spil")
        self.actionOm_gor_sidste_beregning = QtWidgets.QAction(MainWindow)
        self.actionOm_gor_sidste_beregning.setObjectName("actionOm_gor_sidste_beregning")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionAntal_Spillere)
        self.menuMenu.addAction(self.actionNyt_Spil)
        self.menuMenu.addAction(self.actionOm_gor_sidste_beregning)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        
        self.BeregnScore.clicked.connect(self.GetDataForCalcFromWin)

        self.actionAntal_Spillere.triggered.connect(self.AddCol)
        self.Score.horizontalHeader().sectionDoubleClicked.connect(self.SetDeltagerNavne)
        self.actionExit.triggered.connect(lambda: self.ExitGame(MainWindow))
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BeregnScore.setText(_translate("MainWindow", "Beregn"))
        self.ResultatAntalStik.setItemText(0, _translate("MainWindow", "Resultat"))
        self.ResultatAntalStik.setItemText(1, _translate("MainWindow", "13"))
        self.ResultatAntalStik.setItemText(2, _translate("MainWindow", "12"))
        self.ResultatAntalStik.setItemText(3, _translate("MainWindow", "11"))
        self.ResultatAntalStik.setItemText(4, _translate("MainWindow", "10"))
        self.ResultatAntalStik.setItemText(5, _translate("MainWindow", "9"))
        self.ResultatAntalStik.setItemText(6, _translate("MainWindow", "8"))
        self.ResultatAntalStik.setItemText(7, _translate("MainWindow", "7"))
        self.ResultatAntalStik.setItemText(8, _translate("MainWindow", "6"))
        self.ResultatAntalStik.setItemText(9, _translate("MainWindow", "5"))
        self.ResultatAntalStik.setItemText(10, _translate("MainWindow", "4"))
        self.ResultatAntalStik.setItemText(11, _translate("MainWindow", "3"))
        self.ResultatAntalStik.setItemText(12, _translate("MainWindow", "2"))
        self.ResultatAntalStik.setItemText(13, _translate("MainWindow", "1"))
        self.ResultatAntalStik.setItemText(14, _translate("MainWindow", "0"))
        self.ResultatAntalStik.setItemText(15, _translate("MainWindow", "Sol"))
        
        self.TypeMelding.setItemText(0, _translate("MainWindow", "Type"))
        self.TypeMelding.setItemText(1, _translate("MainWindow", "Alm"))
        self.TypeMelding.setItemText(2, _translate("MainWindow", "Goe"))
        self.TypeMelding.setItemText(3, _translate("MainWindow", "Halve"))
        self.TypeMelding.setItemText(4, _translate("MainWindow", "Sans"))
        self.TypeMelding.setItemText(5, _translate("MainWindow", "Vip 1"))
        self.TypeMelding.setItemText(6, _translate("MainWindow", "Vip 2"))
        self.TypeMelding.setItemText(7, _translate("MainWindow", "Vip 3"))
        self.TypeMelding.setItemText(8, _translate("MainWindow", "Sol"))
        self.TypeMelding.setItemText(9, _translate("MainWindow", "Ren Sol"))

        self.StikMelding.setItemText(0, _translate("MainWindow", "Melding"))
        self.StikMelding.setItemText(1, _translate("MainWindow", "13"))
        self.StikMelding.setItemText(2, _translate("MainWindow", "12"))
        self.StikMelding.setItemText(3, _translate("MainWindow", "11"))
        self.StikMelding.setItemText(4, _translate("MainWindow", "10"))
        self.StikMelding.setItemText(5, _translate("MainWindow", "9"))
        self.StikMelding.setItemText(6, _translate("MainWindow", "8"))

        item = self.Score.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Score.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Deltager 1"))
        item = self.Score.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Deltager 2"))
        item = self.Score.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Deltager 3"))
        item = self.Score.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Deltager 4"))
        __sortingEnabled = self.Score.isSortingEnabled()
        self.Score.setSortingEnabled(False)

        self.Score.setSortingEnabled(__sortingEnabled)
 
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAntal_Spillere.setText(_translate("MainWindow", "5 Spillere"))
        self.actionNyt_Spil.setText(_translate("MainWindow", "Nyt Spil"))
        self.actionOm_gor_sidste_beregning.setText(_translate("MainWindow", "Om gor sidste beregning"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

# End SECTION for setting up main window

#Begin SECTION for Game Logic    
    def GetDataForCalcFromWin(self):   # The game state is only kept in the main table. 
        from WhistScoreCalculation import CalculationOfScore  

        Type = self.TypeMelding.currentText()
        Melding = self.StikMelding.currentText()
        Antal = self.ResultatAntalStik.currentText()
        ValidInput = True

        rowPosition = int(self.Score.rowCount()) - 1
        numPlayers = int(self.Score.columnCount())

        PointIRunde = CalculationOfScore(Type, Melding, Antal)
        if PointIRunde == False:
            ValidInput = False
        
        TabereOgVindere = self.LoosersAndWinners(rowPosition, numPlayers)

        if "None" in TabereOgVindere:
            ValidInput = False

        if ValidInput == True:    
            self.AdderPoint(rowPosition, numPlayers, PointIRunde, TabereOgVindere)
            self.AddRowWithCheckBox(rowPosition+1, TabereOgVindere)   #add another Row with checkboxes
            self.ResultatAntalStik.setCurrentIndex(0) # Reset all the bottons on the canvas
            self.TypeMelding.setCurrentIndex(0)
            self.StikMelding.setCurrentIndex(0)  # Reset all the bottons on the canvas
        else:
            self.Flash("Opdater input")

    def AdderPoint(self, row, NumPl, PointIDenneRunde, TabereOgVindere):
        ForrigeScore = [0] * (NumPl)
        if row > 0:
            i=0
            while i<NumPl:
                ForrigeScore[i] = int(self.Score.item(row-1, i).text())
                i += 1

        i = 0
        while i<NumPl:
            item = self.Score.item(row, i)
            item.setText(str((PointIDenneRunde*TabereOgVindere[i])+ForrigeScore[i]))
            i += 1                    

    def LoosersAndWinners(self, row, NumPl):
        i = 0   
        NumOfMeldere = 0
        NumOfModstandere = 0
        NumOfNonParticipants = 0
        mask = [None] * (NumPl+2)
        while i<NumPl:
            item = self.Score.item(row, i)
            if (item.checkState()) == 2:
                NumOfMeldere += 1
                mask[i] = 1
            elif (item.checkState()) == 0 :
                NumOfModstandere += 1
                mask[i] = -1
            elif (item.checkState()) == 1 :
                NumOfNonParticipants += 1
                mask[i] = 0
            i += 1
        mask[i] = NumOfModstandere
        mask[i+1] = NumOfMeldere
        
        if NumOfMeldere == 1:
            i = 0            
            while i<NumPl:
                item = self.Score.item(row, i)
                if (item.checkState()) == 2:
                    mask[i] = 1*3  #apply score weight
                i += 1
        if NumOfModstandere == 1:
            i = 0
            while i<NumPl:
                item = self.Score.item(row, i)
                if (item.checkState()) == 0:
                    mask[i] = -1*3  #apply score weight
                i += 1                    
        if NumOfMeldere == 0 or NumOfModstandere == 0:
            mask = ["None"] * (NumPl + 2)
        
        return mask

    def AddRowWithCheckBox(self, rowNum, mask):
        self.Score.insertRow(rowNum)
        CurrentNumOfPlayers = self.Score.columnCount()
        i = 0
        Index = -100
        if CurrentNumOfPlayers == 5:
            Index = mask.index(0)
            Index += 1
            if Index > 4 :
                Index = 0
        
        while i <CurrentNumOfPlayers:
            PrevItem = self.Score.item(rowNum -1, i)
            PrevItem.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            if CurrentNumOfPlayers == 4:
                item.setCheckState(QtCore.Qt.Unchecked)
            elif CurrentNumOfPlayers == 5:
                if i == Index:
                    item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
                    item.setCheckState(QtCore.Qt.PartiallyChecked)
                else:
                    item.setCheckState(QtCore.Qt.Unchecked)
            self.Score.setItem(rowNum, i, item)
            i += 1

    def AddCol(self):
        CurrentNumOfPlayers = self.Score.columnCount()
        rowPosition = int(self.Score.rowCount())-1
        if CurrentNumOfPlayers <5:
            self.Score.setColumnCount(5)
            
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setText("Deltager 5")
            self.Score.setHorizontalHeaderItem(4, item)

            itemCon = QtWidgets.QTableWidgetItem()
            itemCon.setTextAlignment(QtCore.Qt.AlignCenter)
            itemCon.setCheckState(QtCore.Qt.PartiallyChecked)
            itemCon.setText("0")
            self.Score.setItem(rowPosition, 4, itemCon)
            itemCon.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )

            if rowPosition > 0:
                itemCon1 = QtWidgets.QTableWidgetItem()
                itemCon1.setTextAlignment(QtCore.Qt.AlignCenter)
                itemCon1.setText("0")
                self.Score.setItem(rowPosition - 1, 4, itemCon1)    
                itemCon1.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
        elif CurrentNumOfPlayers == 5:
            self.Flash("Der kan ikke vaere mere end 5 deltagere")
        
# Begin SECTION with functions which open dialog boxes for inputs and error handling

    def Flash(self, Tekst):
        from ErrorMeas import ShowErr
        ShowErr(Tekst)

    def ExitGame(self, Wind):
        from ExirDialog import Ui_Dialog
        ui = Ui_Dialog()
        ui.run(Wind)

    def SetDeltagerNavne(self):
        from InputNavn import Ui_InputNavn
        Tabel = self.Score
        ui =  Ui_InputNavn()
        
        Navn = ui.run()
        ActivSojle = Tabel.currentColumn()
        item = self.Score.horizontalHeaderItem(ActivSojle)
        item.setText(Navn)

# End SECTION with functions which open dialog boxes for inputs and error handling






