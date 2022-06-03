def copie_inverse1(nb_bin):
    ''' Retourne la chaine de caractere nb_bin renversée parcourue de droite à  gauche
    nb_bin : chaine de caractères
    -> Test :
    >>> copie_inverse1('10010')
    '01001'
    '''
    res = ""
    i = len(nb_bin)
    while i > 0:
        i = i - 1 
        res = nb_bin[i] + res  # Inverse l'ordre des lettres
    return res

def copie_inverse2(nb_bin):
    ''' Retourne la chaine de caractere nb_bin renversée parcourue de droite à  gauche
    nb_bin : chaine de caractères
    -> Test :
    >>> copie_inverse1('10010')
    '01001'
    '''
    res = ""
    for el in nb_bin :
        res = el + res
    return res

def conversion(nb, lg):
    '''Conversion decimal -> binaire de nb. Renvoie une chaine de caractere constituée de
    1 et de 0 et de longueur lg si lg est superieur à la longueur de la representation
    binaire de nb.
    >>> conversion(13, 8)
    '00001101'
    >>> conversion(6, 4)
    '0110'
    >>> conversion(6, 2)
    '110'
    '''
    nb_bin = ''
    # Conversion decimale -> binaire par la méthode des divisions successives par 2
    while nb > 0 :
        nb_bin = str(nb%2) + nb_bin
        nb = nb // 2
    nb_bin = str(nb%2) + nb_bin
    # Mise à la longueur lg (ajout de 0 à gauche du nombre
    while lg > len(nb_bin) :
        nb_bin = '0' + nb_bin
    return nb_bin

def booleen(bit) :
    '''Convertit le caractère bit en un booléen : True si bit = '1' / False sinon
    '''
    if bit == '1' :
        return True
    else :
        return False
    
def caractere(bit_bool) :
    '''Convertit le booleen bit_bool en un caractère : '1' si bit_bool = True et False sinon
    '''
    if bit_bool :
        return '1'
    else :
        return '0'
  
    
def addition(nb1, nb2):
    '''Additionne nb1 et nb2 (chaines de caracteres). nb1 et nb2 doivent être de
    même longueur
    '''
    res = ""
    retenue = "0"
    lg = len(nb1)
    while lg > 0 :
        lg = lg - 1
        b1 = booleen(nb1[lg])
        b2 = booleen(nb2[lg])
        r1 = booleen(retenue)
        b3 = b1^b2^r1
        r2 = b1&b2 | b1&r1 | b2&r1
        retenue = caractere(r2)
        res = caractere(b3) + res
    return res

def formate(nb, lg) :
    '''Renvoie le nombre binaire nb sur lg bits si lg est superieur à la longueur
    de nb
    '''
    while len(nb) < lg :
        nb = '0' + nb
    return nb
    
def multiplication (nb1, nb2) :
    ''' multiplie nb1 et nb2
    >>> multiplication("1101", "1011")
    '10001111'
    >>> multiplication("0011", "0011")
    '00001001'
    >>> multiplication("1111", "1111")
    '11100001'
    '''
    lg = len(nb1)
    res = '0'*(2*lg)
    nb1 = formate(nb1, 2*lg)
    while lg > 0 :
        lg = lg - 1
        if nb2[lg] == '1' :
            res = addition(res, nb1)
        nb1 = nb1[1:]+'0'
    return res

