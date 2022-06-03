class GrapheM :
    '''Graphe represente par sa matrice d'adjacence,
    où les sommets sont les entiers o, 1, ..., n-1'''

    def __init__(self, n) :
        self.__n = n
        self.__adj = [[False] * n for _ in range(n)]

    def ajouter_arete(self, s1, s2) :
        '''Ajoute un arc entre les sommets s1 et S2'''
        self.__adj[s1][s2] = True
        self.__adj[s2][s1] = True

    def arete(self, s1, s2) :
        '''Indique la presence d'un arc ou non
        entre s1 et s2'''
        return self.__adj[s1][s2]

    def voisins(self, s) :
        '''Renvoie la liste des voisins de s'''
        v =[]
        for i in range(self.__n) :
            if self.__adj[s][i] :
                v.append(i)
        return v



