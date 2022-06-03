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

def le_plus_frequent(dico, n):
    ''' renvoie le mot le plus frequent de n lettres
    arg : dico -> dictionnaire
        n -> entier
    retour : mot le plus frequent de n lettres
    '''
    cle = ''
    nmax = 0
    for mot in dico:
        if dico[mot] > nmax and len(mot) == n :
            cle = mot
            nmax = dico[mot]
    return cle


def plus_frequents(dico):
    ''' Affcihe les mots les plus longs de 1 à 4 lettres
    '''
    for n in range(1, 5):
        mot = le_plus_frequent(dico, n)
        print(n, " lettre(s) : ",mot ," avec ", dico[mot], " lettres ;")





texteAEtudier = ouvrir_fichier("lesMiserables.txt")
dico = occurences(texteAEtudier)
