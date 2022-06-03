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
    nb_bin = ...
    # Conversion decimale -> binaire par la méthode des divisions successives par 2
    while ...:
        nb_bin = str(...) + nb_bin
        nb = ...
    nb_bin = str(...) + nb_bin
    # Mise à la longueur lg (ajout de 0 à gauche du nombre
    while lg > .... :
        nb_bin = ..........
    return nb_bin

def booleen(bit) :
    '''Converti le caractère bit en un booléen : TRUE si bit = '1' / FALSE sinon
    '''
    
    
    
def caractere(bit_bool) :
    '''Converti le booleen bit_bool en un caractère : '1' si bit_bool = TRUE et FALSE sinon
    '''
  
    
def addition(nb1, nb2):
    '''Additionne nb1 et nb2 (chaines de caracteres). nb1 et nb2 doivent être de
    même longueur.
    >>> addition("0101", "0011")
    '1000'
    >>> addition("1101", "0010")
    '1111'
    >>> addition("1001", "1000")
    '0001'
    '''
    res = ""
    retenue = "0"
    lg = len(nb1)
    while lg > 0 :
        lg = lg - 1
        b1 = booleen(....)
        b2 = ......
        r1 = ......
        b3 = .......
        r2 = ......
        retenue = caractere(r2)
        res = .............
    return res

