# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 21:49:10 2018

@author: herve
"""
import Trie

class mlpl :

    def __init__(self, tirage, dico) :
        '''Construteur :
            parametres : tirage : liste -> Tirage de 7 lettres
                        dico : trie -> Arbre contenant le dictionanire
            Attributs privés :  tirage : list -> Tirage de 7 lettres
                                dictionnaire : Trie -> Dictionnaire dans un trie
        '''
        self.set_tirage(tirage)
        self.set_dico(dico)
        
    def set_tirage(self, tirage) :
        ''' Mutateur de l'attribut prive tirage'''
        self.__tirage = tirage
    
    def get_tirage(self) :
        '''Accesseur à tirage'''
        return self.__tirage
    
    def set_dico(self,dico) :
        '''Mutateur de l'attribut prive dico'''
        self.__dico = dico
    
    def evaluation(self, mot):
        '''Evalue si le mot est dans le dictionnaire
            param : mot : str
            retour : booleen -> True si dans dico
        '''
        return self.__dico.est_dans_arbre(mot)

    def recherche_mots(self, liste_mots,prefixe=''):
        '''Recherche à partir du tirage les mots valides (backtracking)
        parametre : prefixe : str -> debut de la sequence du mot
                    liste_mots : list -> Liste des mots valides
        retour : liste des mots valides
        '''
        for i in range(len(self.__tirage)) :
            lettre=self.__tirage.pop(i)
            prefixe = prefixe+lettre
            if self.evaluation(prefixe) :
                liste_mots.append(prefixe)
            
            self.recherche_mots(liste_mots,prefixe)
            prefixe = prefixe[:-1]
            self.__tirage.insert(i,lettre)
        

    def mot_le_plus_long(self):
        '''retourne la liste des mots le plus long à partir du tirage
        '''
        mots=[]
        mots_les_plus_longs=[]
        self.recherche_mots(mots)
        longueur = [(len(mots[i]),i) for i in range(len(mots))]
        maxi = max(longueur)
        i=1
        for elem in longueur :
            if elem[0] == maxi[0] : mots_les_plus_longs.append(mots[elem[1]])
        return mots_les_plus_longs
                                    
        
        
        

liste_mots = open("dictionnaire.txt", "r").read().split('\n')

dico = Trie.arbreTrie()
dico.construire(liste_mots)
jeu = mlpl(['a','e','s','c','c'],dico)
































