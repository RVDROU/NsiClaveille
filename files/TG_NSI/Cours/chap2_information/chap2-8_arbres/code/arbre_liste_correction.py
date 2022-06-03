
def creation_arbre(r,profondeur):
    ''' r : la racine (str ou int). la profondeur de l’arbre (int)'''
    arbre = [r]+[None for i in range(2**(profondeur+1)-2)]
    return arbre

def insertion_noeud(arbre,n,fg,fd):
    '''Insére les noeuds et leurs enfants dans l’arbre'''
    indice = arbre.index(n)
    arbre[2*indice+1] = fg
    arbre[2*indice+2] = fd

def parent(arbre,p):
    '''Retourne le parent du noeud p de l'arbre'''
    if est_racine(arbre,p) : return None
    if p in arbre:
        indice = arbre.index(p)
        if indice%2 == 0:
            return arbre[(indice-2)//2]
        else:
            return arbre[(indice-1)//2]
def est_vide(arbre) :
    '''Test si l'arbre est vide'''
    return arbre[0]==None

def enfants(arbre,p):
    '''Retourne les enfants du noeud p de l'abre'''
    if p in arbre :
        indice = arbre.index(p)
        if est_feuille(arbre,p) : return (None, None)
        else : return (arbre[2*indice + 1], arbre[2*indice + 2])
    else : return (None, None)

def fils_gauche(arbre,p) :
    '''Retourne le fils gauche du noeud p de l'arbre'''
    return enfants(arbre,p)[0]

def fils_droit(arbre,p) :
    '''Retourne le fils droit du noeud p de l'arbre'''
    return enfants(arbre,p)[1]

def est_racine(arbre,p) :
    '''Test si le noeud p de l'arbre est sa racine'''
    return arbre.index(p) == 0

def est_feuille(arbre,p) :
    '''Test si le noeud p de l'arbre est une feuille'''
    indice = arbre.index(p)
    if 2*indice+1 > len(arbre) or (arbre[2*indice + 1], arbre[2*indice + 2]) == (None, None) : return True
    else : return False

def frere(arbre,p) :
    '''Retourne le frere du noeud p s'il existe'''
    if est_racine(arbre,p) : return None
    pere = parent(arbre,p)
    e = enfants(arbre,pere)
    return e[1-e.index(p)]

# création de l’arbre
arbre = creation_arbre("r",3)
# ajout des noeuds par niveau de gauche à droite
insertion_noeud(arbre,"r","a","b")
insertion_noeud(arbre,"a","c","d")
insertion_noeud(arbre,"b","e","f")
insertion_noeud(arbre,"c",None,"h")
insertion_noeud(arbre,"d","i","j")
insertion_noeud(arbre,"e","k",None)
insertion_noeud(arbre,"f",None,None)