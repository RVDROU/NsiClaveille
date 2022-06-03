def correcteur(clavier, corrige, texte) :
    '''Renvoie le texte corrige
    >>> correcteur('QZAW', 'AWQZ', 'LE ZQGON EST HQWQRDEUX !')
    'LE WAGON EST HAZARDEUX !’
    >>> correcteur('ATB', 'BAT', 'LES ATBETUX SONB AETUX')
    'LES BATEAUX SONT BEAUX'
    '''
    vers = ''
    for l in texte :
        if l in clavier :
            for i in range(len(clavier)) :
                if l == clavier[i] :
                    vers += corrige[i]
        else :
            vers += l
    return vers


def adn(n, seq) :
    '''Renvoie la séquence la plus fréquente
    >>> adn(2, 'TCGTACGTAG')
    'CG'
    >>> adn(4, 'AATTCGGCCGATCGTCGAATTCGATA')
    'AATT'
    '''
    def position(seq, liste_seq) :
        for i in range(len(liste_seq)) :
            if seq == liste_seq[i] :
                return i
        return None
    liste_sous_seq = []
    nombre_sous_seq = []
    for i in range(len(seq)-n) :
        sous_seq = seq[i:i+n]
        if sous_seq in liste_sous_seq :
            index = position(sous_seq, liste_sous_seq)
            nombre_sous_seq[index] += 1
        else :
            liste_sous_seq.append(sous_seq)
            nombre_sous_seq.append(1)
    maxi = 0
    index = 0
    for i in range(len(nombre_sous_seq)) :
        if nombre_sous_seq[i] > maxi :
            maxi = nombre_sous_seq[i]
            index = i
    return liste_sous_seq[index]
        
            
            
        
                
            