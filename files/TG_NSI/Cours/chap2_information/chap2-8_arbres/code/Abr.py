import ArbreBin_correction


class Abr(ArbreBin_correction.ArbreBin) :
    '''Classe arbre binaire de recherche'''
    
    def __init__(self,d, gauche=None, droit=None) :
        ArbreBin_correction.ArbreBin.__init__(self,d, gauche, droit)
        
    def rechercher(self, n : int) :
        '''Recherche la presence de n dans l'arbre'''
        print('entree dans : ',self.noeud())
        if self.noeud() == n : return True
        elif self.est_feuille() : return False
        elif self.noeud() > n : return self.sag().rechercher(n)
        elif self.noeud() <= n : return self.sad().rechercher(n)
        
abr = Abr(35, Abr(20, Abr(10), Abr(25)),Abr(50,Abr(45),Abr(60)))