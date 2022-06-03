class File_recursive :
    
    def __init__(self, val = None , suiv = None):
        self.__valeur = val
        self.__suite = suiv
            
    def __str__(self) :
        if self.__suite == None : return str(self.__valeur)
        else : return str(self.__valeur) + ', ' + self.__suite.__str__()
    
    def __repr__(self) :
        return self.__str__()
    
    def enfiler(self, valeur):
        if self.est_vide() : self.__valeur = valeur
        elif self.__suite == None : self.__suite = File_recursive(valeur, None)
        else : self.__suite.enfiler(valeur)
   
   def defiler(self):
        if self.__valeur == None :
            raise IndexError('File vide')
        elif self.__suite == None :
            val = self.__valeur
            self.__valeur = None
        else :
            val = self.__valeur
            self.__valeur = self.__suite.__get_valeur()
            self.__suite = self.__suite.__get_suivant()
        return val
    
    def __get_valeur(self) :
        return self.__valeur
    
    def __get_suivant(self) :
        return self.__suite

    def est_vide(self):
        return self.__valeur is None
    
f = File_recursive()
f.enfiler(1)
print(f)
f.enfiler(2)
print(f)
f.enfiler(3)
print(f)
f.enfiler(4)
print(f)
f.defiler()
print(f)
f.defiler()
print(f)
f.defiler()
print(f)
f.defiler()
print(f)
f.defiler()
print(f)
f.defiler()
print(f)
