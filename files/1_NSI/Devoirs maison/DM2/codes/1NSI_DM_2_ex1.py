def inverser(l) :
    ''' Change les valeurs de la liste l 
    0 -> 1
    1 -> 0
    '''
    nouvelle_liste = []
    for i in range(len(l)) :
        nouvelle_liste.append(1-l[i])
    return nouvelle_liste


assert inverser([0, 1, 1, 0, 1]) == [1, 0, 0, 1, 0] , 'erreur sur inversion'

