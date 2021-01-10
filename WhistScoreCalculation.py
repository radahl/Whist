# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:01:39 2021

@author: radah
"""

def CalculationOfScore(TypeMelding,MeldtStik,FaktiskeStik):

    MeldingIndex = ["Alm", "Goe", "Halve", "Sans", "Vip 1", "Vip 2", "Vip 3","Sol", "Ren Sol"]
    matching = [s for s in enumerate(MeldingIndex) if TypeMelding in s]
      
    if matching == [] or FaktiskeStik == "Resultat":
        return False
    
    hac = list(matching[(0)])
    Index = int(hac[0])
    SolMelding = False
    if Index>3: #Vip
        Index = Index - 3
        
    if Index > 3: #Sol 
        Index = 0
        SolMelding = True
    
    if SolMelding == False and MeldtStik == "Melding":   # 
        return False        
    
    Scoringstabel = {
        "8": [1, 2, 3, 4],
        "9": [3, 6, 9, 12],
        "10": [7, 14, 21, 28],
        "11": [15, 30, 45, 60],
        "12": [31, 62, 93, 124],
        "13": [63, 126, 189, 254],
        "Sol": [6],
        "Ren Sol" : [14]
        }

    if SolMelding == False:
        forskel = -int(MeldtStik) + int(FaktiskeStik)
        if forskel<0:
            forskel = forskel*2
        else:
            forskel = forskel + 1
        PrisiDenneRunde = Scoringstabel[str(MeldtStik)][Index]*forskel
        if FaktiskeStik ==  "13":
            PrisiDenneRunde = PrisiDenneRunde*2  #Man faar dobbelt op naar man faar 13
    elif SolMelding == True:                       #Alle Sol Meldinger kommer ned i denne branch
        if FaktiskeStik == "Sol": 
            PrisiDenneRunde = Scoringstabel[str(TypeMelding)][Index]
        else:
            PrisiDenneRunde = (-2)*Scoringstabel[str(TypeMelding)][Index]
    else:
        PrisiDenneRunde = False

    
    return PrisiDenneRunde