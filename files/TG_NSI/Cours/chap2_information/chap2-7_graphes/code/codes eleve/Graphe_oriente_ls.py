class Graphe_oriente_ls :
    '''Graphe decrit par un dictionnaire d'adjacence'''
    
    def __init__(self) :
        self.__adj = {}
    
    def __repr__(self) :
        out = ''
        for cle in self.__adj.keys() :
            out += cle + ' -> ' + str(self.__adj[cle])[1:-1] + '\n'
        return out            
    
    def ajouter_sommet(self,s) :
        if s not in self.__adj : self.__adj[s]=[]
        
    def ajouter_arc(self, s1, s2) :
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.__adj[s1].append(s2)
        
    def sommets(self) :
        return list(self.__adj.keys())
    
    def voisins(self, s) :
        return self.__adj[s]

