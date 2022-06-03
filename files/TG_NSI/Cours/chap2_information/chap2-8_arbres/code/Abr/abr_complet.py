class Abr :
    def __init__(self,d, gauche=None, droit=None) :
        '''Construit un arbre binaire de recherche, constituite d'un noeud d'étiquette d, d'un
        sous arbre gauche et un sous arbre droit.
        gauche = None et droit = None par defaut -> construction d'une feuille)'''
        self.data = d
        self.sag = gauche
        self.sad = droit    
    
    def est_feuille(self) :
        '''Retourne vrai si le noeud est une feuille'''
        return self.sag==None and self.sad==None
    
    def nbre_feuilles(self) :
        ''' retourne le nombre de feuilles de l'arbre'''
        if self.est_feuille() : return 1
        elif self.sad == None : return self.sag.nbre_feuilles()
        elif self.sag == None : return self.sad.nbre_feuilles()        
        else : return self.sag.nbre_feuilles() + self.sad.nbre_feuilles()
        
    def nbre_noeuds(self, debug = False) :
        ''' retourne le nombre de noeuds de l'arbre'''
        if self.est_feuille() : return 0
        elif self.sad == None : return self.sag.nbre_noeuds() + 1
        elif self.sag == None : return self.sad.nbre_noeuds()  + 1 
        else : return 1 + self.sag.nbre_noeuds() + self.sad.nbre_noeuds()      
        
    def hauteur(self) :
        '''Renvoie la hauteur de l'arbre'''
        if self.est_feuille() : return 0
        elif self.sad == None : return self.sag.hauteur() + 1
        elif self.sag == None : return self.sad.hauteur()  + 1         
        else : return 1+ max(self.sag.hauteur(), self.sad.hauteur())
        
    def rechercher(self, n : int) :
        '''Recherche la presence de n dans l'arbre'''
        if self.data == n : return True
        elif self.est_feuille() : return False
        elif self.data > n : return self.sag.rechercher(n)
        elif self.data <= n : return self.sad.rechercher(n)

    def inserer(self, n :int) :
        '''Insere n dans l'arbre de recherche'''
        if self.data > n :
            if self.sag == None : self.sag = Abr(n)
            else : self.sag.inserer(n)
        else :
            if self.sad == None : self.sad = Abr(n)
            else : self.sad.inserer(n)
 
     
#Construction d'un arbre de test
abr = Abr(35, Abr(20, Abr(10), Abr(25)),Abr(50,Abr(45),Abr(60)))



#Construction avec inserer() à partir d'une liste
def construire(l) :
    abr = Abr(l.pop(0))
    for i in l :
        abr.inserer(i)
    return abr
        
abr1 = construire([i for i in range(2048)])
abr2 = construire([35,20,50,10,25,45,60])