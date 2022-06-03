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
    Retour : chiffre décimal (entier)
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
        return None
        
def chiffreShadDec2(chiffreShadocks):
    '''Convertit un chiffre Shadocks en décimal  - Version 2
    Arg : chiffreShadocks (string)
    Retour : chiffre décimal (entier)
    '''
    chiffres = ['GA', 'BU', 'ZO', 'MEU']
    if chiffreShadocks in chiffres :
        return chiffres.index(chiffreShadocks)
    else :
        return None
       
    
def convShadDec(nbreShadocks):
    '''Convertit un nombre Shadocks en décimal
    Arg : nbreShadocks : chiffres Shadocks separes par des espaces (string)
    Retour : nombre décimal (entier)
    '''
    result=0
    lstNbreShadocks = decoupeNbreShad(nbreShadocks)
    longueurNbre = len(lstNbreShadocks)

    for i in range(longueurNbre):
        nb = chiffreShadDec(lstNbreShadocks[i])
        result = result+nb*4**(longueurNbre-i-1)
    return result

def convShadDec2(nbreShadocks):
    '''Convertit un nombre Shadocks en décimal Version 2
    Arg : nbreShadocks : chiffres Shadocks separes par des espaces (string)
    Retour : nombre décimal (entier)
    '''
    result=0
    lstNbreShadocks = decoupeNbreShad(nbreShadocks)
    lstNbreShadocks.reverse()
    longueurNbre = len(lstNbreShadocks)

    for i in range(longueurNbre):
        nb = chiffreShadDec(lstNbreShadocks[i])
        result = result+nb*4**i
    return result
