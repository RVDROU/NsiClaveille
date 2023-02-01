def construireDict(listeLiaisons):
    """ listeLiaisons est un tableau de tableaux représentant la liste des  liaisons d'un joueur comme décrit dans le problème
    """
    dictJoueur={}
    for liaison in listeLiaisons :
        villeA = liaison[0]
        villeB = liaison[1]
        if not villeA in dictJoueur.keys() :
            dictJoueur[villeA]=[villeB]
        else :
            destinationsA = dictJoueur[villeA]
            if not villeB in destinationsA :
                destinationsA.append(villeB)
    return dictJoueur


def construireDict_cor(listeLiaisons):
    """ listeLiaisons est un tableau de tableaux représentant la liste des  liaisons d'un joueur comme décrit dans le problème
    """
    dictJoueur={}
    for liaison in listeLiaisons :
        villeA = liaison[0]
        villeB = liaison[1]
        if not villeA in dictJoueur.keys() :
            dictJoueur[villeA]=[villeB]
        else :
            destinationsA = dictJoueur[villeA]
            if not villeB in destinationsA :
                destinationsA.append(villeB)
        
        if not villeB in dictJoueur.keys() :
            dictJoueur[villeB] = [villeA]
        else :
            destinationsA = dictJoueur[villeB]
            if not villeA in destinationsA :
                destinationsA.append(villeA)
    return dictJoueur

def rechercheMinMax(tableau) :
    mini, maxi = tableau[0], tableau[0]
    for elem in tableau :
        if elem < mini :
            mini = elem
        elif elem > maxi :
            maxi = elem
    return {'min' : mini, 'max' : maxi}

liaisonJoueur2 = [['Toulouse', 'Castelnaudary'], ['Toulouse', 'Castres'], ['Castres', 'Mazamet'], ['Castelnaudary', 'Carcassonne']]
tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]