# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 21:49:10 2018

@author: herve
"""
class Morpion :
    '''Jeu du morpion'''
    
    def __init__(self) :
        self.__plateau = self.nouveauPlateau()
    
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
        print(self.__plateau[0],"|",self.__plateau[1],"|",self.__plateau[2],"|")
        print("-----------")
        print(self.__plateau[3],"|",self.__plateau[4],"|",self.__plateau[5],"|")
        print("-----------")
        print(self.__plateau[6],"|",self.__plateau[7],"|",self.__plateau[8],"|")
    
    def nouveauPlateau(self):
        '''Retourne un nouveau plateau vide
        
        ** Test **
        >>> obj.nouveauPlateau()
        ['.','.','.','.','.','.','.','.','.']
        
        '''


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
        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            