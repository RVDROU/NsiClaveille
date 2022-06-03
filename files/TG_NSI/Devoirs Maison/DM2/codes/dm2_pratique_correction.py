import random

def tri_selection(tab) :
    ''' tri par selection d'une liste tab
    tab : liste d'entiers
    retour : tableau tab trié
    '''
    for depart in range(len(tab)-1) :
        i_mini = depart
        for i in range(depart+1, len(tab)) :
            if tab[i] < tab[i_mini] :
                i_mini = i
        tab[depart], tab[i_mini] = tab[i_mini], tab[depart]
    return tab

def occurrence_max(chaine) :
    '''retourne la lettre la plus presente dans un texte chaine
    '''
    def recherche_max(liste) :
        ''' retourne l'indice du nombre max de la liste
        '''
        maxi = 0
        i_maxi = 0
        for i in range(len(liste)) :
            if liste[i] > maxi :
                maxi = liste[i]
                i_maxi = i
        return i_maxi
    
    alphabet = [chr(i) for i in range(97, 122)]
    occurence = [0 for i in range(26)]
    for lettre in chaine :
        if lettre != ' ' :
            occurence[ord(lettre)-97] +=1
    return alphabet[recherche_max(occurence)]
            
def dichotomie(tab, x):
    '''
    tab : tableau trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    '''
    # cas du tableau vide
    if tab == [] :
        return False,1
    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x > tab[-1]) :
        return False,2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (fin+debut)//2
#        print(debut, fin, m, tab[m])
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return False,3            
            
def propager(M, i, j, val):
    if M[i][j]== 0:
        return
    M[i][j]=val
    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)
    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)
    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)
    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)

print(' ##############   Tests des fonctions #####################')

print(' Test de la fonction tri_selection(liste) : ' , end='')
assert tri_selection([1,52,6,-9,12]) == [-9, 1, 6, 12, 52], ('erreur test 1')
liste = [i for i in range(100)]
liste_triee = list(liste)
random.shuffle(liste)
assert tri_selection(liste) ==  liste_triee, ('erreur test 2')
print('ok')

print(' Test de la fonction occurrence_max(ch) : ' , end='')
ch='je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
assert occurrence_max(ch) == 'e', ('erreur test 1')
print('ok')

print(' Test de la fonction dichotomie(tab, x) : ' , end='')
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True, ('erreur test 1')
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) ==  (False, 3), ('erreur test 2')
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],1) == (False, 2), ('erreur test 3')
assert dichotomie([],28) == (False, 1), print('erreur test 3')
print('ok')

print(' Test de la fonction propager(M, i, j, val) : ' , end='')
M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
propager(M,2,1,3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]], ('erreur test 1')
print('ok')
print(' ##############   Tests finis avec succès #####################')



