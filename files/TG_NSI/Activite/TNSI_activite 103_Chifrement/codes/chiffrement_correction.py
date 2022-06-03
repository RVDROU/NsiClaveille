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

def bruteForceKidRSA(e,n) :
    '''casseur de code RSAKid'''
    for d in range (n) :
        if (e*d-1)%n == 0 : return (d,n)

def modinv(e,n) :
    g,x,y = egcd(e,n)
    if g != 1 : return False
    else : return x%n

def egcd(a,b) :
    if a == 0 : return (b, 0 , 1)
    else :
        g,y,x = egcd(b%a,a)
        return (g , x-(b//a)*y, y)

################################# Tests ########################################################################
# Q4
# messageCode = chiffrement_XOR('SPECIALITE NSI', 'CLE')
# messageDecode = chiffrement_XOR(messageCode, 'CLE')
#
# Q8
# (clePublique, clePrivee) = genere_cles_publique_privee(13, 32, 69, 35)
# messageChiffre = chiffre_message('NSI', clePublique)
# messageDechiffre = dechiffre_message(messageChiffre, clePrivee)
#
# Q11
(d,n) = bruteForceKidRSA(53447,5185112)
#
# Q13
e,n = 230884490440319, 194326240259798261076
d = modinv(e,n)
deuxiemeMessage = dechiffre_message([16623683311702968, 19625181687427115, 16392798821262649, 16392798821262649,\
20548719649188391, 7388303694090208, 17547221273464244, 15931029840382011, 19163412706546477, 7388303694090208, \
15238376369061054, 18239874744785201, 18008990254344882, 19163412706546477, 7388303694090208, 19394297196986796, \
19625181687427115, 20548719649188391, 15007491878620735, 19625181687427115, 20317835158748072, 7388303694090208, \
7619188184530527] , (d, n))