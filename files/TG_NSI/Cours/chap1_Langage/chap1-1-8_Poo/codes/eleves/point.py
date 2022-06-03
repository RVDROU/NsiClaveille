from math import *

class Point :
    '''Classe de definition d'un point en coordonnees
    polaires et cartesiennes
    '''
    def __init__(self, x, y) :
        # Q3
                
        
    def lire_coord_cartesiennes(self) :
        return                       #Q2
    
    def lire_coord_polaires(self) :
        return                       #Q2
    
    def __convertir_cart_polaire(self) :
        #Calcul de theta
        if self.__x > 0 : self.__theta = atan(self.__y/self.__x)
        elif self.__x < 0 and self.__y >=0 : self.__theta = atan(self.__y/self.__x) + pi
        elif self.__x < 0 and self.__y < 0 : self.__theta = atan(self.__y/self.__x) - pi
        elif self.__x == 0 and self.__y > 0 : self.__theta = pi/2
        elif self.__x == 0 and self.__y < 0 : self.__theta = -pi/2
        else : self.__theta = 0
        
        # Calcul de r
        self.__r = sqrt(self.__x**2 + self.__y**2)
            
            