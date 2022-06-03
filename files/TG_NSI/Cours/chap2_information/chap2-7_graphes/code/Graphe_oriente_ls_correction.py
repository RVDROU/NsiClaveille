class Graphe_pondere :
    '''Graphe pondere decrit par un dictionnaire d'adjacence'''
    
    def __init__(self) :
        self.__adj = {}
    
    def __repr__(self) :
        out = ''
        for cle in self.__adj.keys() :
            out += cle + ' -> ' + str(self.__adj[cle])[1:-1] + '\n'
        return out            
    
    def ajouter_sommet(self,s) :
        ''' Ajoute un sommet s au graphe'''
        if s not in self.__adj : self.__adj[s]=[]
        
    def ajouter_arete(self, s1, s2,poids) :
        ''' Ajoute une arete et son poids entre s1 et s2'''
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.__adj[s1].append((s2,poids))
        self.__adj[s2].append((s1,poids))
        
    def arc_existe(self, s1, s2) :
        '''Retourne vrai si une arete existe entre s1 et s2'''
        return s2 in self.__adj[s1]
    
    def sommets(self) :
        '''Retourne la liste des sommets'''
        return list(self.__adj.keys())
    
    def voisins(self, s) :
        '''Retourne la liste des voisins de s'''        
        return [sommet[0] for sommet in self.__adj[s]]
    
    def poids(self,s1, s2) :
        '''Retourne le poids de l'arete entre s1 et s2 si elle existe. None sinon'''
        if s2 not in self.voisins(s1) : return None
        else :
            i = self.voisins(s1).index(s2)
            return self.__adj[s1][i][1]
    
def charger_aretes(graph, aretes) :
    for a in aretes :
        graph.ajouter_arete(a[0], a[1], a[2])
        
aretes = [('R1','R2',0.1), ('R1','R3',1), ('R2','R3',0.1), ('R3','R5',0.1), ('R2','R4',1), ('R4','R5',0.1), \
          ('R4','R6',0.1), ('R5','R7',10), ('R5','R6',1), ('R6','R7',1)]

network = Graphe_pondere()
charger_aretes(network,aretes)