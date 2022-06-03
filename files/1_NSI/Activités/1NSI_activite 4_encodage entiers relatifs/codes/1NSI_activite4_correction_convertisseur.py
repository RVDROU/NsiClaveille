''' Convertisseur d'entiers relatifs en binaire signe avec lecomplement a 2
convertir_dec_binaire(5) renvoie [0, 1, 0, 1]
convertir_dec_binaire(-5) renvoie [1, 0, 1, 1]
'''


def complNbreBin(nbreBin) :
    ''' Complemente nbreBin
    Arg -> nbreBin : nombre binaire. Liste d'entiers 1 / 0
    retour ->  Liste d'entiers 1 / 0
    Ex : complNbreBin([0,1,1,0,1,0,0,1]) renvoie [1,0,0,1,0,1,1,0]
    '''
    for i in range(len(nbreBin)) :
        nbreBin[i] = 1 - nbreBin[i]
    return nbreBin


def additionBinaire(b1,b2) :
    ''' Additionne b1 à b2
    Arg ->  b1 : bit (entier 1 /0)
            b2 : bit (entier 1 /0)
    retour -> retenue et resultat (entiers 1 /0)
    Ex : additionBinaire(1,1) renvoie (1,0)
    '''
    retenue = (b1+b2)//2
    result = (b1+b2)%2
    return [retenue,result]


# def ajout1(nbreBin) :
#     ''' SOLUTION 1
#     Ajoute 1 au nombre binaire nbreBin
#     Arg -> nbreBin : nombre binaire. Liste d'entiers 1 / 0
#     retour ->  Liste d'entiers 1 / 0
#     Ex : ajout1([1,0,0,1,1]) renvoie [1,0,1,0,0]
#     '''
#     lg = len(nbreBin)-1
#     c = 1
#     while lg > 0 :
#         c , nbreBin[lg] = additionBinaire(nbreBin[lg],c)
#         lg-=1
#     return nbreBin

def ajout1(nbreBin) :
    ''' SOLUTION 2
    Ajoute 1 au nombre binaire nbreBin
    Arg -> nbreBin : nombre binaire. Liste d'entiers 1 / 0
    retour ->  Liste d'entiers 1 / 0
    Ex : ajout1([1,0,0,1,1]) renvoie [1,0,1,0,0]
    '''
    retenue = 1
    liste_result = [0] * len(nbreBin)
    for i in range(len(nbreBin)) :
        indice = -i-1
        res_addition = additionBinaire(retenue, nbreBin[indice])
        res = res_addition[1]
        retenue = res_addition[0]
        liste_result[indice]=res
    return liste_result


def convertir_dec_binNaturel(nbreDecimal) :
    ''' Convertir en binaire naturel nbreDecimal
    Arg -> nbreDecimal : nombre entier naturel
    retour ->  Liste d'entiers 1 / 0
    '''
    nbreBin = []
    res = nbreDecimal
    while res > 0 :
        nbreBin.append(res%2)
        res = res//2
    nbreBin.append(0)
    nbreBin.reverse()
    return nbreBin

def val_abs(n):
    '''Calcul la valeur absoule de n'''
    if n>=0 :
        return n
    else :
        return -n


def convertir_dec_binaire(nbreDecimal) :
    ''' Convertir en binaire signe complement a 2 nbreDecimal
    Arg -> nbreDecimal : nombre entier relatif
    retour ->  Liste d'entiers 1 / 0 (complement a 2)
    '''
    nbreBin = convertir_dec_binNaturel(val_abs(nbreDecimal))
    if nbreDecimal > 0 :
        return nbreBin
    else :
        nbreBinComplemente = complNbreBin(nbreBin)
        nbreBin = ajout1(nbreBinComplemente)
        return nbreBin
