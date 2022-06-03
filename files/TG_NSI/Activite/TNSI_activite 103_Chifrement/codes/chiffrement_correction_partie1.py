def chiffrement_XOR(message, cle) :
    '''chiffre le message avec cle par un chiffrement symetrique XOR
    cle doit etre de dtaille inférieure ou égale à message
    '''
    cle_formattee = cle * (len(message)//len(cle)) + cle[:(len(message)%len(cle))+1]
    message_chiffre = ''
    for i in range(len(message)) :
        message_chiffre += chr(ord(message[i]) ^ ord(cle_formattee[i]))
    return message_chiffre

def genere_cles_publique_privee(a1, b1, a2, b2) :
    ''' génère et retourne la clef publique (n,e) et la clef secrète (n,d)
    à partir des 4 entiers passés en paramètre a1, b1, a2, b2
    '''
    M = a1*b1-1
    e = a2*M+a1
    d = b2*M+b1
    n = int((e*d-1)/M)
    return ((e,n),(d,n))

def chiffre_message(m,clef) :
    '''chiffre un message m qui est une chaîne de caractères avec la clé clef,
    en remplaçant chaque caractère par son code ASCII en décimal. 
    Le message chiffré retourné est une liste de nombres. La taille de la liste
    étant égale à la longueur de la chaine de caractères m
    '''
    message_chiffre = []
    for lettre in m :
        message_chiffre.append((ord(lettre)*clef[0])%clef[1])
    return message_chiffre

def dechiffre_message(m,clef) :
    '''déchiffre un message m qui est une liste de nombres et renvoie le message
    déchiffré sous la forme d'une chaîne de caractères.
    '''
    message = ''
    for lettre in m :
        message+= chr((lettre*clef[0])%clef[1])
    return message



################################# Tests ########################################################################
# Q4
# messageCode = chiffrement_XOR('SPECIALITE NSI', 'CLE')
# messageDecode = chiffrement_XOR(messageCode, 'CLE')
#
# Q8
# (clePublique, clePrivee) = genere_cles_publique_privee(13, 32, 69, 35)
# messageChiffre = chiffre_message('NSI', clePublique)
# messageDechiffre = dechiffre_message(messageChiffre, clePrivee)
