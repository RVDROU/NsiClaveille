import pile

class File :
    def __init__(self) :
        self.__f = pile.Pile()
        
    def __repr__(self):
        return str(self.__f)
    
    def enfiler(self, e) :
        self.__f.empiler(e)
        
        
    def defiler(self) :
        p_sec = pile.Pile()
        
        while not(self.__f.est_vide()) :
            p_sec.empiler(self.__f.depiler())
        e = p_sec.depiler()
        while not(p_sec.est_vide()) :
            self.__f.empiler(p_sec.depiler())
        return e   
        
    
    def est_vide(self) :
        return self.__f.est_vide()
        

        