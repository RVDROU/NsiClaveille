def voy(l) :
    '''Indique si l est une voyelle '''
    voyelles = 'aeiouy'
    return l in voyelles

def dentiste(texte) :
    ''' Renvoie le texte sans les consonnes'''
    res =''
    for l in texte :
        if voy(l) :
            res = res + l
    return res
            