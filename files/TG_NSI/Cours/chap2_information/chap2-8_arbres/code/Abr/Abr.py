import ArbreBin


class Abr(ArbreBin.ArbreBin) :
    '''Classe arbre binaire de recherche.'''
    
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
        if self.noeud() > n :
            if self.sag() == None : self.set_sag(Abr(n))
            else : self.sag().inserer(n)
        else :
            if self.sad() == None : self.set_sad(Abr(n))
            else : self.sad().inserer(n)
            
      
#Construction d'un arbre de test
abr = Abr(20, Abr(15, Abr(7), Abr(19,Abr(16,None,Abr(17)),None)),\
              Abr(40,None,Abr(60,Abr(50),Abr(70))))

def test_rechercher_Abr(abr,list_tests, list_resultats) :
    ''' Test automatique de la méthode Abr.rechercher()
    abr : arbre binaire de recherche
    list_tests : liste des valeurs (int) à rechercher
    list_resulats : lsite des resultats (booleens) attendus
    Retour : Pas de retour attendu -> Levée d'erreur par assertion si test faux'''
    for i in range(len(list_tests)):
        assert abr.rechercher(list_tests[i]) == list_resultats[i], 'erreur sur '+str(list_tests[i])


# 
# #Construction avec inserer() à partir d'une liste
# def construire(l) :
#     abr = Abr(l.pop(0))
#     for i in l :
#         abr.inserer(i)
#     return abr
#         
# abr1 = construire([i for i in range(2048)])
# abr2 = construire([10, 20, 25, 35, 45, 50, 60])
