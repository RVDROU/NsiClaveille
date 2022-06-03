# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:27:56 2019

@author: herve
"""

from manipulationImage import *				
img=ouvrirImage("imageSimple.png")			
hauteur=len(img)							
largeur=len(img[0])							
for ligne in range(hauteur) :					
    for colonne in range(largeur) :			
        img[ligne][colonne]=255		