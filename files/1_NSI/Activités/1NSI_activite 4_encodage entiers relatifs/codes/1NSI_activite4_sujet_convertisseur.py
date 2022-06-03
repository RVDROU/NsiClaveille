''' Convertisseur d'entiers relatifs en binaire signe avec lecomplement a 2
convertir_dec_binaire(5) renvoie [0, 1, 0, 1]
convertir_dec_binaire(-5) renvoie [1, 0, 1, 1]
'''



def additionBinaire(b1,b2) :
    ''' Additionne b1 à b2
    Arg ->  b1 : bit (entier 1 /0)
            b2 : bit (entier 1 /0)
    retour -> retenue et resultat (entiers 1 /0)
    Ex : additionBinaire(1,1) renvoie (1,0)
    '''


    return (carry,result)


def ajout1(nbreBin) :
    ''' Ajoute 1 au nombre binaire nbreBin
    Arg -> nbreBin : nombre binaire. Liste d'entiers 1 / 0
    retour ->  Liste d'entiers 1 / 0
    Ex : ajout1([1,0,0,1,1]) renvoie [1,0,1,0,0]
    '''


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


def convertir_dec_binaire(nbreDecimal) :
    ''' Convertir en binaire signe complement a 2 nbreDecimal
    Arg -> nbreDecimal : nombre entier relatif
    retour ->  Liste d'entiers 1 / 0 (complement a 2)
    '''
