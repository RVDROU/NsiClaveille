class arbreTrie:
    '''Classe arbre Trie'''
    def __init__(self, lettre=None):
        self.__lettre = str(lettre)       # Lettre du noeud
        self.__fin = False                # Le noeud est la fin d'un mot 
        self.__suivants = {}              # Noeuds suivants. Clé du dictionnaire : valeur du noeud (lettre)

    def get_suivant(self, lettre : str) -> object:
        ''' Renvoie le noeud (objet arbreTrie) de valeur lettre qui suit le noeud courant'''
        return self.__suivants.get(lettre)
    
    def liste_suivants(self) -> list :
        '''Retourne la liste des lettres suivantes'''
        pass
    
    def get_lettre(self) -> str:
        '''Renvoie la lettre du noeud courant'''
        pass
    
    def est_fin_mot(self) -> bool:
        ''' Indique si le noeud est la fin d'un mot'''
        pass
        
    def set_fin_mot(self):
        '''Mutateur de l'attribut fin -> Affecte True à fin'''
        pass
        
    def ajout_noeud(self, lettre : str):
        '''Ajoute un noeud (objet arbreTrie) de valeur lettre dans la liste des suivants avec la clé : lettre'''
        pass
        
    def construire(self, liste_mots : list) :
        '''Construit un arbre Trie à partir d'une liste de mots '''
        for mot in liste_mots:
            node = self                         # Affecte dans node la racine de l'arbre
            mot = mot.rstrip()                  # Retire espaces du mot
            for lettre in mot:
                if lettre not in node.liste_suivants() :
                    node.ajout_noeud(lettre)
                node = node.get_suivant(lettre) # Avance dans l'arbre
            node.set_fin_mot()

    def est_dans_arbre(self, mot : str) -> bool:
        ''' Test si le mot est dans l'arbreTrie '''
        pass

