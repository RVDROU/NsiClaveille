# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 21:49:10 2018

@author: herve
"""
class Morpion :
    '''Jeu du morpion'''

    def __init__(self,n) :
        self.__plateau = self.nouveauPlateau(n)

    def __repr__(self ):
        return str(self.__plateau)

    def setPlateau(self, val) :
        '''Mutateur de __plateau pour debuggage'''
        self.__plateau = val

    def getPlateau(self) :
        '''Accesseur à __plateau'''
        return self.__plateau

    def afficherPlateau(self):
        '''Affiche l'etat du plateau sur la console'''
        if len(self__plateau)==9 :
            print(self.__plateau[0],"|",self.__plateau[1],"|",self.__plateau[2],"|")
            print("-----------")
            print(self.__plateau[3],"|",self.__plateau[4],"|",self.__plateau[5],"|")
            print("-----------")
            print(self.__plateau[6],"|",self.__plateau[7],"|",self.__plateau[8],"|")
        else :
            print(self.__plateau[0],"|",self.__plateau[1],"|",self.__plateau[2],"|",self.__plateau[3],"|")
            print("--------------")
            print(self.__plateau[4],"|",self.__plateau[5],"|",self.__plateau[6],"|",self.__plateau[7],"|")
            print("--------------")
            print(self.__plateau[8],"|",self.__plateau[9],"|",self.__plateau[10],"|",self.__plateau[11],"|")

    def nouveauPlateau(self,n):
        '''Retourne un nouveau plateau vide

        ** Test **
        >>> obj.nouveauPlateau()
        ['.','.','.','.','.','.','.','.','.']

        '''
        return n*['.']

    def jouer(self, joueur : str, positionCoup : int):
        '''Joue le coup de joueur à la positionCoup
        Parametre : joueur(str) ->'x' ou 'o'
                    positionCoup (int) -> Compris entre 0 et 8
        '''
        self.__plateau[positionCoup]=joueur


    def analyserPlateau(self) :
        '''Recherche un vainqueur
        Retour : tuple -> (vainqueur : bool, nom du vainqueur : str)

        ** Test **
        >>>obj.setPlateau(['x','.','.','x','.','.','x','.','.'])
        >>>obj.analyserPlateau()
        (True, 'x')
        >>>obj.setPlateau(['o','.','.','.','o','.','.','.','o'])
        >>>obj.analyserPlateau()
        (True, 'o')
        >>>obj.setPlateau(['o','o','o','.','.','.','.','.','.'])
        >>>obj.analyserPlateau()
        (True, 'o')
        >>>obj.setPlateau(['.','.','.','.','o','.','.','.','o'])
        >>>obj.analyserPlateau()
        (False, None)

        '''
        if len(self.__plateau) == 12 :
            coupsGagnants=[[0,1,2],[1,2,3],[4,5,6],[5,6,7],[8,9,10],[9,10,11],[0,4,8],[1,5,9],[2,6,10],[3,7,11],[2,5,8],[3,6,9],[0,5,10],[1,6,11]]
        else :
            coupsGagnants=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        
        for i in coupsGagnants:
            if self.__plateau[i[0]] is not '.' and self.__plateau[i[0]]==self.__plateau[i[1]]==self.__plateau[i[2]]:
                return (True,self.__plateau[i[0]])
        return(False,None)

    def tourDeJouer(self):
        '''Indique le nom du joueur qui doit jouer ('x' commence la partie)
        Retour : nom joueur (str) -> 'x' ou 'o'
        '''
        if self.__plateau.count('x')==self.__plateau.count('o'):
            return('x')
        else:
            return('o')

    def plateauComplet(self):
        ''' teste si plateau plein
        Retour : plateauPlein (bool)

        ** Test **
        >>>obj.setPlateau(['x','.','.','x','.','.','x','.','.'])
        >>>obj.plateauComplet()
        False
        >>>obj.setPlateau(['o','x','x','x','o','o','x','o','o'])
        >>>obj.plateauComplet()
        True
        '''
        return(not('.' in self.__plateau))

    def coupsRestants(self):
        '''Liste les coups possibles
        Retour : liste des index des cases libres (int)

        ** Test **
        >>>obj.setPlateau(['x','.','.','x','.','.','x','.','.'])
        >>>obj.coupsRestants()
        [1,2,4,5,7,8]
        >>>obj.setPlateau(['o','x','x','x','o','o','x','o','o'])
        >>>obj.coupsRestants()
        []
        '''
        return([i for i in range(len(self.__plateau)) if self.__plateau[i]=='.'])






















