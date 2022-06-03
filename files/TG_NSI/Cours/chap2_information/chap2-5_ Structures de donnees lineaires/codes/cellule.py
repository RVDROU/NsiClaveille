class cellule :
    
    def __init__(self, val, suivant) :
        self.__valeur = val
        self.__suivant = suivant
    
    def __str__(self) :
        return '(' + str(self.__valeur) + ', ' + str(self.__suivant) + ')'
    
    def __repr__(self) :
        return self.__str__()
    
    def modifier_suivant(self, val) :
        self.__suivant = val
    
    def modifier_valeur(self,val) :
        self.__valeur = val
        
    def lire_suivant(self) :
        return self.__suivant
    
    def lire_valeur(self) :
        return self.__valeur