videos = [('Video 1', 114, 4.57), ('Video 2', 32, 0.630),
('Video 3', 20, 1.65), ('Video 4', 4, 0.085),
('Video 5', 18, 2.15), ('Video 6', 80, 2.71),
('Video 7', 5, 0.320)]

def decoupe(l1):
    '''Decoupe une liste l1 en deux parties egales
    par utilisation de slices '''
    milieu = len(l1)//2
    return l1[:milieu], l1[milieu:]

def fusion(l1, l2, selection_critere) :
    '''Fusionne 2 listes triees l1 et l2'''
    l = []
    while len(l1)>0 and len(l2) :
        if selection_critere(l1) < selection_critere(l2) : l.append(l2.pop(0))
        else : l.append(l1.pop(0))
    return l + l1 + l2

def tri_fusion(l, choix) :
    '''Trie la liste l par la methode tri par fusion'''
    
    def selection_taille(l) :
        return l[0][2]

    def selection_duree(l) :
        return l[0][1]

    def selection_duree_sur_taille(l) :
        return l[0][1]/l[0][2]
    
    l1, l2 = decoupe(l)
    if len(l1) > 1 : l1 = tri_fusion(l1, choix)
    if len(l2) > 1 : l2 = tri_fusion(l2, choix)
    
    fonctions = {'duree' : selection_duree, 'taille':selection_taille, 'd/t' : selection_duree_sur_taille}
    return fusion(l1,l2, fonctions[choix])

def binaire(n, nb) :
    '''renvoie la valeur binaire de n sur nb bits'''
    n_bin = bin(n)[2:]
    return '0'* (nb-len(n_bin)) + n_bin

def ens_des_parties(ensemble) :
    '''Construit toutes les combinaisons possibles de l'ensemble
    retour : liste des ensembles (liste de combinaisons)
    '''
    n = 2**len(ensemble)
    combinaisons =[]
    for i in range(1, n) :
        sous_ensemble = []
        n_bin = binaire(i, len(ensemble))
        for j in range(len(n_bin)) :
            if n_bin[j] == '1' :
                sous_ensemble.append(ensemble[j])
        combinaisons.append(sous_ensemble)
    return combinaisons

def recherche(parties, contrainte) :
    '''Recherche la solution optimale suivant la contrainte de taille par la méthode brut force
    >>> recherche(ss_ensemble, 5)
    [('Video 2', 32, 0.63), ('Video 3', 20, 1.65), ('Video 6', 80, 2.71)]

    '''
    resultats = []
    for ss_ens in parties :
        taille = 0
        duree = 0
        for video in ss_ens :
            taille += video[2]
            duree += video[1]
        
        resultats.append((ss_ens, taille, duree))
        maxi = 0
    for each in resultats :
        if each[2]>maxi and each[1] < contrainte :
            maxi = each[2]
            optimal = each[0]
            res = each
    print(res)
    return optimal

def glouton(videos, taille, choix) :
    '''Recherche une solution acceptable au problème de choix de vidéo suivant leur longueur (
    (problème de type sac à dos), résolu par méthode glouton
    '''
    assert choix in ['duree', 'taille', 'd/t'] , 'Parametre choix inconnu'
    films_tries = tri_fusion(videos, choix)
    cumul_taille = 0
    ss_ensemble = []
    for film in films_tries :
        if not(cumul_taille + film[2] > taille) :
            cumul_taille = cumul_taille + film[2]
            ss_ensemble.append(film)
    return ss_ensemble, cumul_taille
        
        
        
for t in ['duree', 'taille', 'd/t'] :
    print(t, '   -> ', glouton(videos, 5, t))

# recherche(ens_des_parties(videos), 5)
       