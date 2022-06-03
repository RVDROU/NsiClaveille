# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 21:49:10 2018

@author: herve
"""
import Morpion
import runtest
        

class MorpionIA(Morpion.Morpion) :
    
    def __init__(self) :
        '''MorpionIA hérite des méthodes/attributs de Morpion'''
        Morpion.Morpion.__init__(self)
        self.memo = {}
        
    def adversaire(self,joueur):
        '''Renvoie le joueur adverse du joueur
        Retour : joueur adeverse (str) -> 'x' ou '.'
        '''
        return {'x' : 'o', 'o' : 'x'}[joueur]

    def evaluationStatique(self):
        '''Evalue la situation du plateau (+10,-10,0, None)
        
        ** Test **
        >>>obj.setPlateau(['x','.','.','x','.','.','x','.','.'])
        >>>obj.evaluationStatique()
        10    
        >>>obj.setPlateau(['o','o','o','x','x','.','x','.','.'])
        >>>obj.evaluationStatique()
        -10
        >>>obj.setPlateau(['o','x','x','x','o','o','o','o','x'])
        >>>obj.evaluationStatique()
        0
        >>>obj.setPlateau(['o','x','.','.','.','.','.','.','o'])
        >>>obj.evaluationStatique()
        >>>
        '''        
        gagne,gagnant=self.analyserPlateau()    
       
        if gagnant=='x': return 10
        elif gagnant=='o' : return -10
        elif self.plateauComplet()==True: return 0
        else : return None

        
    def evaluerCoup(self, joueur,positionCoup):
        ''' Evalue un nouveau coup
            Paramètres : joueur (str) : 'x' ou 'o'
                         positionCoup (int) : position sur la grille intervalle [0;8]
            retour : evaluation du coup : None, +10 , -10, 0
        '''
        self.jouer(joueur,positionCoup)    
        return self.evaluationStatique()

                     
    def minmax(self,joueur):
        '''Identifie le meilleur coup (algo Min_Max)
        Parametre : joueur (str) : 'x', 'o'
        retour : position du meilleur coup (int)
        
        ** Test **
        >>>obj.setPlateau(['x','x','o','.','o','.','x','.','.'])
        >>>obj.minmax('o')
        (0,3)    
        >>>obj.setPlateau(['x','x','o','o','o','.','x','.','.'])
        >>>obj.minmax('x')
        (0,5)
          
        
        '''
        scoreBranches = [] #Liste des scores de chaque branche 
        for coup in self.coupsRestants():
            score=self.evaluerCoup(joueur,coup)
            
            if score==None:
                score,_=self.minmax(self.adversaire(joueur) )
         
            scoreBranches.append((score,coup))
            self.jouer('.', coup)  # efface le coup joué
        
        if joueur=='x' : return max(scoreBranches)
        else : return min(scoreBranches)
    
    def minmax_memo(self,joueur):
        '''Identifie le meilleur coup (algo Min_Max)
        Parametre : joueur (str) : 'x', 'o'
        retour : position du meilleur coup (int)
        
        ** Test **
        >>>obj.setPlateau(['x','x','o','.','o','.','x','.','.'])
        >>>obj.minmax('o')
        (0,3)    
        >>>obj.setPlateau(['x','x','o','o','o','.','x','.','.'])
        >>>obj.minmax('x')
        (0,5)
          
        
        '''
        scoreBranches = [] #Liste des scores de chaque branche 
        for coup in self.coupsRestants():
                      
            score=self.evaluerCoup(joueur,coup)
            if score==None:
                ##### Test si la cas est dans le dico de memoisation
                if ','.join(self.getPlateau()) in self.memo :
                    #### Si oui retourne le score sans tester les sous arbres
                    score = self.memo[','.join(self.getPlateau())]
                    
                    #### Efface le coup joué
                    self.jouer('.', coup)
                    return score

                score,_=self.minmax_memo(self.adversaire(joueur) )

         
            scoreBranches.append((score,coup))
            self.jouer('.', coup)  # efface le coup joué
        
        if joueur=='x' :
            score = max(scoreBranches)
            ######  Ajout de la memorisation du score si 'x' joue
            self.memo[','.join(self.getPlateau())] = score
            ######
            return score
        else :
            score = min(scoreBranches)
            ######  Ajout de la memorisation du score si 'o' joue
            self.memo[','.join(self.getPlateau())] = score
            ######
            return score
           

            
            



            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            