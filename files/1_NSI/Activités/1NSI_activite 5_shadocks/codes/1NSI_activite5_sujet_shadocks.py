# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:21:56 2018

@author: herve
"""

def decoupeNbreShad(nombreShadocks):
    '''Decoupe le nombre Shadock en une liste de chiffres
    Arg -> nb : nombre shadocks (string)
    Retour -> Liste de chiffres Shadocks (liste de strings) 
    '''
    nbreDecoupe = nombreShadocks.split(' ')
    return nbreDecoupe
    
    
def chiffreShadDec(chiffreShadocks):
    '''Convertit un chiffre Shadocks en décimal
    Arg : chiffreShadocks (string)
    Retour : chiffre décimal (entier) / 'error' si chiffre inconnu
    '''
    if chiffreShadocks == "GA":
        return 0
    elif chiffreShadocks == "BU":
        return 1
    elif chiffreShadocks == "ZO":
        return 2
    elif chiffreShadocks == "MEU":
        return 3
    else :
        return 'error'
        
  