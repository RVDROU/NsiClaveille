def max2(val1, val2) :
    ''' renvoie la valeur la plus garnde entre val1 et val2'''
    if val1 > val2 :
        return val1
    else :
        return val2
    
def max3(val1, val2, val3) :
    '''Renvoie la valeur la plus grande entre trois valeurs'''
    return max2(val1, max2(val2, val3))

def max3b(val1, val2, val3) :
    '''Renvoie la valeur la plus grande entre trois valeurs
    -> Solution 2'''
    max1 = max2(val2, val3)
    resultat = max2(max1, val1)
    return resultat