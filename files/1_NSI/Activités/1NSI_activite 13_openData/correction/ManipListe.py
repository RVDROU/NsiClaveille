# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:07:53 2020

@author: herve
"""

### Programme de chargement d un fichier csv dans une variable (variable table) ###

import csv

file = open("liste.csv")
table = list(csv.DictReader(file,delimiter=","))
table = [dict(elem) for elem in table]
file.close()
dico = table[0]
tab=[]
for i in dico :
    tab.append(i)