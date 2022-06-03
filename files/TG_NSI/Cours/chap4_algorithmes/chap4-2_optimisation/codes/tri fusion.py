# Methodes d'optimisation / Diviser pour régner
#               Le tri fusion
#################################################
#Lycee Claveille - Périgueux -

def decoupe(l1):
    '''Decoupe une liste l1 en deux parties egales
    par utilisation de slices '''
    milieu = len(l1)//2
    return l1[:milieu], l1[milieu:]

def decoupe2(l1) :
    '''Decoupe une liste l1 en deux parties egales
    par itération '''
    milieu = len(l1)//2
    l1a = []
    l1b = []    
    for i in range(milieu) :
        l1a.append(l1[i])
    for i in range(milieu, len(l1)) :
        l1b.append(l1[i])
    return l1a, l1b
        
def decoupe3(l1) :
    '''Decoupe une liste l1 en deux parties egales
    par comprehension de liste '''
    milieu = len(l1)//2        
    return [l1[i] for i in range(milieu)], [l1[i] for i in range(milieu, len(l1))]
        
def fusion(l1, l2) :
    '''Fusionne 2 listes triees l1 et l2'''
    l = []
    while len(l1)>0 and len(l2) :
        if l1[0] > l2[0] : l.append(l2.pop(0))
        else : l.append(l1.pop(0))
    return l + l1 + l2

def tri_fusion(l) :
    '''Trie la liste l par la methode tri par fusion'''
    l1, l2 = decoupe(l)
    if len(l1) > 1 : l1 = tri_fusion(l1)
    if len(l2) > 1 : l2 = tri_fusion(l2)
    return fusion(l1,l2)

def generateur_liste(n) :
    import random
    liste = [i for i in range(n)]
    random.shuffle(liste)
    return liste