class Avare :
    ''' Classe Avare :
    Caractérisé par sa fortune et son nom
    '''    
    def __init__(self, name, fortune) :
        self.__nom = name
        self.__fortune = fortune
        
    def __repr__(self) :
        return 'Fortune de ' + self.__nom + ' : ' + str(self.__fortune) +' $'
    
    def compter(self) :
        return self.__fortune
    
    def depenser(self,somme) :
        self.__fortune -= 0.9*somme # Un avar ne depense jamais trop....
    
    def encaisser(self,somme) :
        self.__fortune += somme
        
        