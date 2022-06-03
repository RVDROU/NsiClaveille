import ArbreBin


class Abr(ArbreBin.ArbreBin) :
    '''Classe arbre binaire de recherche
    -> herite des methodes de ArbreBin'''
    
    def __init__(self,d, gauche=None, droit=None) :
        ArbreBin.ArbreBin.__init__(self,d, gauche, droit)
        
    def rechercher(self, n : int) :
        '''Recherche la presence de n dans l'arbre'''
        print('entree dans : ',self.noeud())
        if self.noeud() == n : return True
        elif self.noeud() > n :
            if self.sag() == None : return False
            else : return self.sag().rechercher(n)
        else :
            if self.sad() == None : return False
            else : return self.sad().rechercher(n)

    def inserer(self, n :int) :
        '''Insere n dans l'arbre de recherche'''
        pass
            
            
def test_rechercher_Abr(abr, list_tests, list_resultats) :
    ''' Test automatique de la méthode Abr.rechercher()
    abr : arbre de recherche
    list_tests : liste des valeurs (int) à rechercher
    list_resulats : lsite des resultats (booleens) attendus
    Retour : Pas de retour attendu -> Levée d'erreur par assertion si test faux'''
    pass
      