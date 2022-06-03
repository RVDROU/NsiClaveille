# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:57:07 2019

@author: herve
"""

from random import *							
#Choix du joueur

joueur = int(input('Votre choix ?\n[1] : Pierre\n[2] : Feuille\n[3] : Ciseaux'))
print('Vous avez choisi',end= ' ')
if joueur == 1 :
    print('pierre')				
elif joueur == 2:				
    print('feuille')				
else :						
    joueur = 3					
    print('ciseaux')