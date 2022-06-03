def hamming(t1, t2):
    ''' t1 et t2 sont deux tableaux de même taille, constitués d'entiers'''
    d = 0
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            d = d + 1
    return d