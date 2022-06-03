import bisect
class ArbreHuffman:
    '''Défini un arbre d'Huffmann.
    Paramètres : lettre -> Lettre de la racine de l'arbre (str)
                 nbocc -> nombre d'occurrence de la lettre (int)
                 g -> sous arbre gauche (None par defaut)____
                 d -> sous arbre droit (None par defaut) ____|-> Feuille
    '''                 
    def __init__(self, lettre:str, nbocc:int, g=None, d=None):
        self.lettre = lettre
        self.nbocc = nbocc
        self.gauche = g
        self.droite = d
    
    def __repr__(self) :
        if self.est_feuille() :
            return '|'+self.lettre +':' + str(self.nbocc)+'|'
        elif self.lettre == None:
            return  '|'+'none'+':'+str(self.nbocc)+','+self.gauche.__repr__()+','+self.droite.__repr__()+'|'
        else :
            return  '|'+self.lettre+':'+str(self.nbocc)+','+self.gauche.__repr__()+','+self.droite.__repr__()+'|'
    
    def __lt__ (self, other) -> bool :
    # Un arbre A est strictement inférieur à un arbre B si le nombre d’occurrences
    #indiqué dans A est strictement supérieur à celui de B
        return self.nbocc > other.nbocc
    
    def est_feuille(self) -> bool :
        return

def parcours(arbre:ArbreHuffman, chemin_en_cours:list, dico:dict):
    '''Parcourt en profondeur l'arbre d'Huffman et attribut le code
    aux différents noeuds suivant leur position dans l'arbre
    Paramètres : arbre : Arbre d'Huffman parcouru en profondeur
                chemin en cours : code en cours sur le noeud
                dico : dictionnaire lettres : codes
    '''
    if arbre is None: return
    elif arbre.est_feuille(): dico[arbre.lettre] = 
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)


def fusionne(gauche:ArbreHuffman, droite:ArbreHuffman) -> ArbreHuffman:
    '''Fusionne gauche et droite dans un arbre '''
    nbocc_total=
    return ArbreHuffman(       )

def compte_occurrences(texte: str) -> dict:
    '''Renvoie un dictionnaire avec chaque caractere du texte comme clé et
    le nombre d’apparition de ce caractere dans le texte en valeur
    >>> compte occurrences ("AABCECA" )
    {"Av: 3, "BU: 1, “C": 2, "E": 1}
    '''
    occ = {}
    for caract in texte:
        if caract not in occ:
            
        else :                
            occ[caract] += 1
    return 

def construit_liste_arbres(texte: str) -> list:
    ''' Renvoie une liste d’arbres de Huffman, chacun réduit à une feuille
    >>> construit_liste_arbres('AAABB')
    [|A:3|,|B:2|]
    '''
    dic_occurrences = compte_occurrences(texte)
    liste_arbres = []
    for
    
    return 

def codage_huffman(texte: str) -> dict:
    ''' Codage de Huffman optimal à partir d’un texte
    >>> codage huffman("AAAABBBBBCCD" )
    {'A': [0, 0], 'C': [0, 1, 0], 'D': [0, 1, 1], 'B': [1]}
    '''
    liste_arbres = construit_liste_arbres(texte)
    # Tri par nonbres d’occurrences décroissants
    liste_arbres.sort()
    # Tant que tous les arbres n’ont pas été fusionnés
    while len(liste_arbres) > 1:
        ## Les deux plus petits nombres d’occurrences
        # sont à la fin de la liste
        droite = liste_arbres.pop()
        gauche = liste_arbres.pop()
        new_arbre = fusionne(gauche, droite)
        # Le module bisect permet d’insérer le nouvel
        # arbre dans la liste, de manière à ce que la
        # liste reste triée
        bisect.insort(liste_arbres, new_arbre)
    # A la fin il n'en reste qu'un : notre arbre d'Huffman
    arbre_huffman = liste_arbres.pop()
    # Parcours de l’arbre pour relever les codes
    dico = {}
    parcours(arbre_huffman, [], dico)
    return dico
# Script principal
with open("texte.txt") as f:
    texte = f.read()
print (codage_huffman(texte))