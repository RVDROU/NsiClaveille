class arbreTrie:
    '''Classe arbre Trie'''
    def __init__(self, lettre=None):
        self.__lettre = str(lettre)       # Lettre du noeud
        self.__fin = False                # Le noeud est la fin d'un mot 
        self.__suivants = {}              # Nooeuds suivants

    def get_suivant(self, lettre : str) -> object:
        ''' Renvoie l'object noeud suivant de valeur lettre'''
        return self.__suivants.get(lettre)
    
    def liste_suivants(self) :
        '''Retourne la liste de suivants'''
        return list(self.__suivants.keys())
    
    def get_lettre(self) -> str:
        '''Renvoie la lettre du noeud courant'''
        return self.__lettre

    def est_fin_mot(self) -> bool:
        ''' Indique si le noeud est la fin d'un mot'''
        return self.__fin
        
    def set_fin_mot(self):
        '''Mutateur de l'attribut fin -> Affecte True à fin'''
        self.__fin = True
        
    def ajout_noeud(self, lettre : str):
        '''Ajoute un noeud de valeur lettre dans la liste des suivants avec la clé : lettre'''
        self.__suivants[lettre]=arbreTrie(lettre)
        
    def construire(self, liste_mots : list) -> object:
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
        node = self                             # Affecte dans node la racine de l'arbre
        for lettre in mot:
            if lettre in node.liste_suivants() :
                node = node.get_suivant(lettre) # Avance dans l'arbre
            else:
                return False
        return node.est_fin_mot()

# liste_mots = open("dictionnaire.txt", "r").read().split('\n')
# 
# dico = arbreTrie()
# dico.construire(liste_mots)
# 
# class mlpl :
#     
#     def __init__(self) :
#         self.__dico=Trie().makeTrie(open("dictionnaire.txt", "r").read().split('\n'))
# 
#     
#     def rechercher_mots(self, tirage) :
#         def mots_selon_tirage(tirage, liste_mots, prefixe= '') :
#             for i in range(len(tirage)) :
#                 lettre = tirage.pop(i)
#                 print(tirage, 'lettre : ',lettre)
#                 if self.__dico.inTrie(prefixe+lettre) : liste_mots.append(prefixe+lettre)
#                 if len(tirage)>0 : mots_selon_tirage(tirage, liste_mots, prefixe+lettre)
#                 print (tirage, end=' / ')
#                 tirage.insert(i, lettre)
#                 print('retour', tirage)
#         
#         liste_mots = []
#         mots_selon_tirage(tirage,liste_mots)
#         return liste_mots
#         

