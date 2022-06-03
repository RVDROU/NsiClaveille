# -*- coding: utf-8 -*-
from miserables_eleve import *

texteAEtudier = ouvrir_fichier("lesMiserables.txt")
dico = occurences(texteAEtudier)

""" Réponses par Adrien JAYAT le 27/02/20 """
############################### Question 1 ######################################
nbMots = len(dico)
print("Les Misérables contiennent {} mots différents".format(nbMots))

############################# Question 2 et 3 ###################################
def mot_le_plus_frequent(dico: dict, n=None) -> (str, int):
    maxValue = 0
    mot = ''
    for m,o in dico.items():
        if o>maxValue and (not(n) or len(m)==n): #2e partie de la condition pour Q3
            maxValue = o
            mot = m
    return mot, maxValue, n

mot, occur, n = mot_le_plus_frequent(dico)
print("Le mot le plus fréquent est '{}' avec {} occurences".format(mot, occur))

############################### Question 3 ######################################
mot, occur, n = mot_le_plus_frequent(dico, 19)
print("Le mot le plus fréquent de {n} lettres est '{}' avec {} occurence(s)".format(mot, occur, n=n))

############################### Question 4 ######################################
def plus_frequents(dico: dict, nb: int):
    for n in range(1, nb+1):
        mot, occur, n = mot_le_plus_frequent(dico, n)
        print("{n} lettre(s) : {mot} avec {nb}".format(n=n, mot=mot, nb=occur))

plus_frequents(dico, 4)

############################### Question 5 ######################################
nbLettres = max(map(len, dico))
print("Il y a", nbLettres, "lettres maximum à traiter")
