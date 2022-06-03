count = 0
def cherche(texte, motif) :
    '''Cherche les positions des occurences d'un motif dans un texte
    attributs -> texte et motif : str
    retour -> Liste des indices de départ de la chaîne motif dans texte
    '''
    global count
    n = len(texte)
    p = len(motif)
    i = 0
    positions = []
    while i + p <= n :
        correspond, decalage = correspondance(texte, motif, i)
        print('(', count, ')     ', i, ' : ', texte[i], ' -> ', decalage)
        if correspond :
            positions.append(i)
        i = i + decalage
    return positions

def correspondance_a(texte, motif, i) :
#    global count
    p, n = len(motif), len(texte)
    assert i + p <= n
    for j in range(p):
#        count += 1
#        print('(', count, ')', i, ' : ', texte[i + j], ' <-> ', motif[j])
        if texte[i + j] != motif[j] :
            return (False, 1)
    return (True, 1)

def correspondance(texte, motif, i) :
    global tab_dec, count
    p, n = len(motif), len(texte)
    for j in range(p - 1, -1, -1) :
        x = texte[i + j]
        count += 1
        if x != motif[j] :
            if x in tab_dec[j] :
                k = tab_dec[j][x]
            else :
                k = -1
            return (False, j - k)
    return (True, 1)
    
def construire_table_decalage(motif) : 
    global tab_dec
    tab_dec = [{} for _ in range(len(motif))]
    for j in range(len(motif)) :
        for k in range(j) :
            tab_dec[j][motif[k]] = k

            
txt = 'chercher, rechercher et chercher encore'
motif = 'chercher'
construire_table_decalage(motif)