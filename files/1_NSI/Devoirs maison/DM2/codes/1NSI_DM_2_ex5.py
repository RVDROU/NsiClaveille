def nombre_positifs(t) :
    ''' Renvoie le nombre d'éléments positifs de la liste t
    >>> nombre_positifs([7, -2, 5, 6, -10])
    3
    '''
    n = 0
    for e in t :
        if e > 0 :
            n = n + 1
    return n

def compte_lettres(l, texte) :
    '''Renvoie le nombre de fois que l est présent dans texte
    l : caractere
    texte : chaine de caracteres
    >>> compte_lettres('a', 'blablacar')
    3
    >>> compte_lettres('b', 'blablacar')
    2
    '''
    n = 0
    for e in texte :
        if e == l :
            n = n + 1
    return n

def fois_10(t) :
    '''Multiplie par 10 les trois dernieres valeurs de t
    >>> fois_10([5, 2, 3, 8])
    [20, 30, 80]
    '''
    derniers = t[-3:]
    for i in range(3) :
        derniers[i] = derniers[i] * 10
    return derniers

def fois_10_v2(t) :
    '''Multiplie par 10 les trois dernieres valeurs de t
    >>> fois_10_v2([5, 2, 3, 8])
    [20, 30, 80]
    '''
    derniers = []
    for i in range(len(t)-3, len(t)) :
        derniers.append(t[i] * 10)
    return derniers

assert nombre_positifs([7, -2, 5, 6, -10, 0]) == 3, 'nbre_positifs faux'
assert compte_lettres('a', 'blablacar') == 3 , 'compte_lettre faux, test 1'
assert compte_lettres('b', 'blablacar') == 2 , 'compte_lettre faux, test 2'
assert fois_10([5, 2, 3, 8]) == [20, 30, 80] , 'fois_10 faux'
print('####### Tests termines #################################')