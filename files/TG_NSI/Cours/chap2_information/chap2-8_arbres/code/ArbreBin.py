class ArbreBin :
    def __init__(self,d, gauche=None, droit=None) :
        '''Construit un arbre constituite d'un noeud d'étiquette d, d'un
        sous arbre gauche et un sous arbre droit.
        gauche = None et droit = None par defaut -> construction d'une feuille)'''
        self.__data = d
        self.__sag = gauche
        self.__sad = droit

    def __str__(self) :
        return '{'+str(self.__sag) +'_'+ '('+self.__data +')'+'_'+str(self.__sad)+'}'

    def __repr__(self) :
        return self.__str__()

    def est_feuille(self) :
        '''Retourne vrai si le noeud est une feuille'''
        return self.__sag==None and self.__sad==None

    def sag(self) :
        '''retorune le sous arbre gauche'''
        return self.__sag

    def sad(self) :
        '''retorune le sous arbre droit'''
        return self.__sad

    def noeud(self) :
        '''retorune l'etiquette du noeud'''
        return self.__data

def creer_noeud(abr_lst,indice) :
    '''Convertir d'un arbre defini par une liste en un arbre de type AbreBin
    parametres : abr_lst -> Liste d'etiquettes des noeuds d'un arbre binaire
                 indice : indice dans la liste du noeud à creer
    sortie :     Arbre de type ArbreBin
    '''
    fg = abr_lst[2*indice+1]
    fd = abr_lst[2*indice+2]
    if fg is None and fd is None :
        return ArbreBin(abr_lst[indice])
    elif fg is None and fd is not None :
        return ArbreBin(abr_lst[indice], None, creer_noeud(abr_lst, 2*indice+2))
    elif fg is not None and fd is None :
        return ArbreBin(abr_lst[indice], creer_noeud(abr_lst, 2*indice+1), None)
    else : return ArbreBin(abr_lst[indice], creer_noeud(abr_lst, 2*indice+1), creer_noeud(abr_lst, 2*indice+2))




abr = creer_noeud(['N','Y', 'O', 'D', 'V', 'T', 'H', 'C','O', None,None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],0)

