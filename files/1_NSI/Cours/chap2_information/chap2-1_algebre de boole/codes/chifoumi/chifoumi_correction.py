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
    
#Choix de la machine
ordi=randint(1,3)
print('Je joue',end= ' ')
if ordi == 1 :
    print('pierre')				
elif ordi == 2:				
    print('feuille')				
else :						
    print('ciseaux')
    
#Recherche gagnant
if joueur == ordi :
    print('Egalité!')
elif ((joueur==1 and ordi==3) or (joueur==2 and ordi==1) or (joueur==3 and ordi==2)):
    print('Vous avez gagné')
else : 
    print('Vous avez perdu')