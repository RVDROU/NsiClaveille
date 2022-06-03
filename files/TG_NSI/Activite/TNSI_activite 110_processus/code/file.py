class File :
    ''' Classe File : Structure de données lineaire de type file'''
    
    def __init__(self) :
        self.__f = []
          
    def enfiler(self, e) :
        ''' Enfile e dans la structure'''
        self.__f.append(e)
        
        
    def defiler(self) :
        '''Retire un element de la file'''
        return self.__f.pop(0)
        
    
    def est_vide(self) :
        ''' Retourne vrai si la file est vide'''
        return len(self.__f) == 0
    
    def nb_elements(self) :
        '''Retourne le nombre d'éléments contenu dans la file'''
        return len(self.__f)
        

        