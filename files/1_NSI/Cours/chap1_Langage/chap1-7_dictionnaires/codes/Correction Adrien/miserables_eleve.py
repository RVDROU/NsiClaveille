# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:36:23 2020

@author: herve
"""

def occurences(texte: str) -> dict:
    ''' Compte le nombre d’occurence de chaque mot d’un texte
    arg : texte : texte a etudier
    retour : dictionnaire des mots (cle type str) associes au nombre d’occurence
    '''
    import re
    texte = re.split('\W+', texte) #enleve ponctuations et split le texte
    dico_occur = {}

    for mot in texte:
        mot = mot.lower() # convertit le mot en minuscule
        if dico_occur.get(mot): # teste si mot connu
            dico_occur[mot] += 1
        else:
            dico_occur[mot] = 1
    return dico_occur

def ouvrir_fichier(fichier: str) -> str:
    ''' Retourne le texte contenu dans un fichier texte
    Arg : fichier : non du fichier txt
    Retour : texte
    '''
    with open(fichier, 'r', encoding='utf-8') as f:
        texte = f.read()
    return texte

texteAEtudier = ouvrir_fichier("lesMiserables.txt")
dico = occurences(texteAEtudier)