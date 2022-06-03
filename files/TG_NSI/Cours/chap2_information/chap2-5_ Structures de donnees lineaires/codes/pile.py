class Pile :
    def __init__(self) :
        self.__n = 20
        self.__p = [None] * self.__n
        self.__p[0] = 1
        
    def __repr__(self):
        return str(self.__p)
    
    def empiler(self, e) :
        if self.__p[0] < self.__n :
            self.__p[self.__p[0]] = e
            self.__p[0] +=1
        else :
            raise IndexError('Pile pleine')
        
    def depiler(self) :
        if self.__p[0] > 1 :
            e = self.__p[self.__p[0] - 1]
            self.__p[self.__p[0] - 1] = None
            self.__p[0] -=1
            return e
        else :
            raise IndexError('Pile vide')
            
        
    
    def est_vide(self) :
        if self.__p[0] == 1 :
            return True
        else :
            return False
        

        