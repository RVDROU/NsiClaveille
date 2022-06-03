# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:36:23 2020

@author: herve
"""

def occurences(texte):
    ''' Compte le nombre d’occurence de chaque mot d’un texte
    arg : texte : texte a etudier (string)
    retour : dictionnaire des mots (cle type str) associes au nombre d’occurence
    (valeur type int)
    '''
    dico_occur = {}
    for mot in texte.split():
        mot = mot.lower() # convertit le mot en minuscule
        mot = mot.strip(",.;!?-()«»_") # enleve ponctuations collees aux mots
        if mot in dico_occur: # teste si mot connu
            dico_occur[mot] += 1
        else:
            dico_occur[mot] = 1
    return dico_occur

def ouvrir_fichier(fichier):
    ''' Retourne le texte contenu dans un fichier texte
    Arg : fichier : non du fichier txt
    Retour : texte (type str)
    '''
    with open(fichier, 'r', encoding='utf-8') as f:
        texte = f.read()
    return texte

texteAEtudier = ouvrir_fichier("lesMiserables.txt")
dico = occurences(texteAEtudier)
