# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:36:23 2020

@author: herve
"""
import time

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
    with open(fichier, 'r',encoding='utf-8') as f:
        texte = f.read()
    return texte
    
def mot_le_plus_frequent(dico) :
    '''Recherche l occurrence la plus frequente
    arg : dico -> dictionnaire
    retour : mot le plus frequent
    '''
    cle = ''
    nmax = 0
    for mot in dico:
        if dico[mot] > nmax :
            cle = mot
            nmax = dico[mot]
    return cle
    
def mot_le_plus_long(dico) :
    '''Recherche l occurrence la plus longue
    retour : mot le plus frequent
    '''
    cle = ''
    nmax = 0
    for mot in dico:
        if len(mot) > nmax :
            cle = mot
            nmax = len(mot)
    return cle,nmax

def complexite_in(dico,nb):
    t0=time.time()
    for i in range(nb) :
        if 'the' in dico :
            a=0
    return time.time()-t0
    
def complexite_get(dico,nb):

    t0=time.time()
    for i in range(nb) :
        if dico.get('the'):
            a=0
    return time.time()-t0

        
    
    
    
    
    
texteAEtudier = ouvrir_fichier("lesMiserables.txt")
dico = occurences(texteAEtudier)
