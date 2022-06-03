# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 21:49:10 2018

@author: herve
"""

class mlpl :

    def __init__(self, tirage, dico) :
        '''Construteur :
            parametres : tirage : liste -> Tirage de 7 lettres
                        dico : trie -> Arbre contenant le dictionanire
            Attributs privés :  tirage : list -> Tirage de 7 lettres
                                dictionnaire : Trie -> Dictionnaire dans un trie
        '''
    def set_tirage(self, tirage) :
        ''' Mutateur de l'attribut prive tirage'''
        pass
    
    def get_tirage(self) :
        '''Accesseur à tirage'''
        pass
    
    def set_dico(self,dico) :
        '''Mutateur de l'attribut prive dico'''
        pass
    
    def evaluation(self, mot):
        '''Evalue si le mot est dans le dictionnaire
            param : mot : str
            retour : booleen -> True si dans dico
        '''
        pass

    def recherche_mots(self,prefixe='', liste_mots=[]):
        '''Recherche à partir du tirage les mots valides (backtracking)
        parametre : prefixe : str -> debut de la sequence du mot
                    liste_mots : list -> Liste des mots valides
        retour : liste des mots valides
        '''
        pass

    def mot_le_plus_long(self):
        '''retourne la liste des mots le plus long à partir du tirage
        '''
        pass


































