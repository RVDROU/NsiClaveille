from carte import *
import random

class Jeu2Cartes :
    ''' Jeu de 52 cartes'''
    
    def __init__(self) :
        self.rassembler_cartes()
    
    def __repr__(self) :
        jeu_complet = ''
        for carte in self.__jeu :
            jeu_complet += str(carte) + ' ,'
        return jeu_complet
        
    def melanger_cartes(self) :
        random.shuffle(self.__jeu)
        
    def rassembler_cartes(self) :
        self.__construire_jeu()
        self.melanger_cartes()
        self.__nbre_cartes=len(self.__jeu)
        
    def distribuer_carte(self) :
        carte = self.__jeu.pop()
        self.__nbre_cartes -= 1
        return carte
    
    def __construire_jeu(self) :
        self.__jeu = [0]*52
        i = 0
        for coul in ['carreau', 'coeur', 'pique', 'trefle'] :
            for val in range(2,15):
                self.__jeu[i] = Carte(val,coul)
                i +=1
    
