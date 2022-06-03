''' Probleme du rendu de monnaie resolu par méthode itérative
-----
Lycee Claveille
'''
def rendu_monnaie_glouton_ver1(somme, pieces  = [5,2,1,0.5,0.2,0.1]) :
    ''' Algorithme du rendu de monnaie avec boucle while
    Attributs : somme (float) : somme à rendre
                pieces : liste de pieces disponibles ordonnées par ordre décroissant
    Retour : liste avec le nombre de pièces de meme rang que pieces'''
    def est_trie(liste) :
        for i in range(len(liste)-1) :
            if liste[i] <= liste[i+1] :
                return False
        return True
       
    assert est_trie(pieces), 'les pieces doivent etre triee'
    rendu_monnaie=[]
    indice_piece = 0
    while somme > 0 :
        if pieces[indice_piece] > somme :
            indice_piece += 1            
        else :
            rendu_monnaie.append(pieces[indice_piece])
            somme = round(somme - pieces[indice_piece],2)
        # print('i : ',indice_piece, ', piece :',pieces[indice_piece],', somme : ', somme)
    return rendu_monnaie


def rendu_monnaie_glouton_ver2(somme, pieces = [5,2,1,0.5,0.2,0.1]) :
    ''' Algorithme du rendu de monnaie avec boucle while
    Attributs : somme (float) : somme à rendre
                pieces : liste de pieces disponibles ordonnées par ordre décroissant
    Retour : liste avec le nombre de pièces de meme rang que pieces'''
    rendu_monnaie=[]
    indice_piece = 0
    while somme > 0 :
        while pieces[indice_piece] > somme :
            indice_piece += 1            
        rendu_monnaie.append(pieces[indice_piece])
        somme = round(somme - pieces[indice_piece],2)
        # print('i : ',indice_piece, ', piece :',pieces[indice_piece],', somme : ', somme)
    return rendu_monnaie

def rendu_monnaie_glouton_ver3(somme, pieces  = [5,2,1,0.5,0.2,0.1]):
    ''' Algorithme du rendu de monnaie avec boucle while
    Attributs : somme (float) : somme à rendre
                pieces : liste de pieces disponibles ordonnées par ordre décroissant
    Retour : liste avec le nombre de pièces de meme rang que pieces'''
    def nb_piece(somme, piece) :
        '''Retourne le nombre de piece optimal pour rendre somme
        '''
        return (int(somme // piece))

    rendu_monnaie = []            
    for i in range(len(pieces)) :
        nb = nb_piece(somme, pieces[i]) 
        somme = round(somme - nb*pieces[i],2)
        rendu_monnaie += nb*[pieces[i]]
        # print('i : ',i, ', piece :',pieces[i],', somme : ', somme)
    return rendu_monnaie


def rendu_monnaie_glouton_recursif(somme, pieces = [5,2,1,0.5,0.2,0.1]) :
    ''' Algorithme du rendu de monnaie avec boucle while
    Attributs : somme (float) : somme à rendre
                pieces : liste de pieces disponibles ordonnées par ordre décroissant
    Retour : liste avec le nombre de pièces de meme rang que pieces'''
    def nb_piece(somme, piece) :
        '''Retourne le nombre de piece optimal pour rendre somme
        '''
        return (int(somme // piece))
    
    if len(pieces) == 0 :
        return []
    else :
        nb = nb_piece(somme, pieces[0])
        somme = round(somme-nb*pieces[0],2)
        return [nb]+rendu_monnaie_glouton_recursif(somme, pieces[1:])
