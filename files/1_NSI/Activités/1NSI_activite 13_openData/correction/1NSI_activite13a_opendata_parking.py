# -*- coding: utf-8 -*-
"""
Programme listant les parking publics de Bordeaux et le nombre de place
"""

import csv

file = open("bor_sigparkpub.csv")
table = list(csv.DictReader(file,delimiter=";"))
file.close()
for ligne in table :
    print(ligne['nom'] +' : ' +ligne['nombre_de_places'] )
 
