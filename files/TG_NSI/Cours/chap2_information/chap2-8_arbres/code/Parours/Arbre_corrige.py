import file

class Arbre :
    def __init__(self,d, gauche=None, droit=None) :
        '''Construit un arbre constituite d'un noeud d'étiquette d, d'un
        sous arbre gauche et un sous arbre droit.
        gauche = None et droit = None par defaut -> construction d'une feuille)'''
        self.__data = d
        self.__sag = gauche
        self.__sad = droit
    
    def __str__(self) :
        return str(self.__data)
    
    def est_feuille(self) :
        '''Retourne vrai si le noeud est une feuille'''
        return self.__sag==None and self.__sad==None

    def parcours_infixe(self) :
        '''Affiche les etiquettes des noeuds en suivant un parcours infixe'''
        if self.est_feuille() :
            print(self.__data, end = ' ' )
            return
        else :
            self.__sag.parcours_infixe()
            print(self.__data, end = ' ')
            self.__sad.parcours_infixe()
            
    def parcours_postfixe(self) :
        '''Affiche les etiquettes des noeuds en suivant un parcours postfixe'''
        if self.est_feuille() :
            print(self.__data, end = ' ' )
            return
        else :
            self.__sag.parcours_postfixe()
            self.__sad.parcours_postfixe()
            print(self.__data, end = ' ')
            
    def parcours_prefixe(self) :
        '''Affiche les etiquettes des noeuds en suivant un parcours prefixe'''
        if self.est_feuille() :
            print(self.__data, end = ' ' )
            return
        else :
            print(self.__data, end = ' ')
            self.__sag.parcours_prefixe()
            self.__sad.parcours_prefixe()

    def parcours_largeur(self) :
        '''Affiche les etiquettes des noeuds en suivant un parcours en largeur'''
        f = file.File()
        f.enfiler(self)
        while not f.est_vide() :
            print('    Contenu file :',str(f))
            abr = f.defiler()
            if not abr.est_feuille() :
                f.enfiler(abr.__sag)
                f.enfiler(abr.__sad)
                
            print(abr.__data)



def creer_noeud(abr_lst,indice=0) :
    '''Convertir d'un arbre defini par une liste en un arbre de type AbreBin
    parametres : abr_lst -> Liste d'etiquettes des noeuds d'un arbre binaire complet
                 indice : indice dans la liste du noeud à creer
    sortie :     Arbre de type ArbreBin
    '''
    fg = abr_lst[2*indice+1]
    fd = abr_lst[2*indice+2]
    if fg is None and fd is None :
        return Arbre(abr_lst[indice])
    elif fg is None and fd is not None :
        return Arbre(abr_lst[indice], None, creer_noeud(abr_lst, 2*indice+2))
    elif fg is not None and fd is None :
        return Arbre(abr_lst[indice], creer_noeud(abr_lst, 2*indice+1), None)
    else : return Arbre(abr_lst[indice], creer_noeud(abr_lst, 2*indice+1), creer_noeud(abr_lst, 2*indice+2))

abr = creer_noeud(['H', 'Y', 'N', 'P', 'T', 'O', '.', None, None, None, None, None, None, None, None])
