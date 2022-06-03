def tri_par_selection(t):
    '''trie le tableau t dans l'ordre croissant'''
    for debut_nonTriee in range(len(t)):
        indice_valMini =  debut_nonTriee
        for i in range(debut_nonTriee + 1 , len(t)):
            if t[i] < t[indice_valMini]:
                indice_valMini = i
        echange(t,  debut_nonTriee, indice_valMini)
        
def echange(table, indice1, indice2):
    '''Echange de position les deux elements aux indices
    indice 1 et indice 2 de table.
    Exemple :   >>> table = [1, 2, 3, 4]
                >>> echange(table, 0, 1)
                >>> table
                [2, 1, 3, 4]
    '''
    temp = table[indice1]
    table[indice1] = table[indice2]
    table[indice2] = temp
    

def insere(t, i, val):
    ''' insère val dans la liste triée t[0...i[ supposée triée'''
    indice_val = i
    while indice_val > 0 and t[indice_val - 1] > val :
        t[indice_val] = t[indice_val - 1]
        indice_val = indice_val - 1
    t[indice_val] = val

    
def tri_insertion(t) :
    '''trie le tableau t dans ordre croissant'''
    for i in range(1, len(t)) :
        insere(t, i, t[i])
