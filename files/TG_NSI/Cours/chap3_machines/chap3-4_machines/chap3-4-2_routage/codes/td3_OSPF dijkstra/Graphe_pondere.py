class Graphe_pondere :
    '''Graphe pondere decrit par un dictionnaire d'adjacence'''
    
    def __init__(self) :
        '''Attribut -> __adj : dictionnaire d'adjacence'''
        self.__adj = {}
    
    def __repr__(self) :
        out = ''
        for cle in self.__adj.keys() :
            out += cle + ' -> ' + str(self.__adj[cle])[1:-1] + '\n'
        return out            
    
    def ajouter_sommet(self,s) :
        ''' Ajoute un sommet s au graphe si il n'existe pas'''
        if s not in self.__adj : self.__adj[s]=[]
        
    def ajouter_arete(self, s1, s2,poids) :
        ''' Ajoute une arete et son poids entre s1 et s2
        Les noeuds s1 et s2 sont crees si besoin'''
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.__adj[s1].append((s2,poids))
        self.__adj[s2].append((s1,poids))
        
    def arc_existe(self, s1, s2) :
        '''Retourne vrai si une arete existe entre s1 et s2'''
        for sommet in self.__adj[s1] :
            if sommet[0] == s2 : return True
        return False
    
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

def test_graphe() :
    ''' Test la methode graphe_pondere() en verifiant les resultats obtenus a partir d'un graphe de référence'''
    # Construction du graphe de reference
    network = Graphe_pondere()
    network.ajouter_arete('R1', 'R2', 0.1)
    network.ajouter_arete('R1', 'R3', 1)

    
    # Verification de la methode sommets() (test complet donné en exemple)
    assert sorted(network.sommets()) == ['R1', 'R2', 'R3'] , 'Erreur dans la liste des sommets'
    
    # Verification de la methode arc_existe -> 1 test vari et 1 test faux
    assert network.arc_existe('R1', 'R2') == True, "Erreur de test d'arete"
    assert network.arc_existe('R2', 'R3') == False, "Erreur de test d'arete"
    
    # Verification des voisins de R1 puis ceux de R2
    assert sorted(network.voisins('R1')) == ['R2', 'R3'] , 'Erreur dans la liste des voisins'
    assert network.voisins('R2') == ['R1'] , 'Erreur dans la liste des voisins'
    
    # Verification du poids des deux aretes
    assert network.poids('R1','R2') == 0.1 , 'Erreur de poids'
    assert network.poids('R1','R3') == 1 , 'Erreur de poids'
    
    print('Test fini sans erreur')
    

def charger_aretes(graph, aretes) :
    for a in aretes :
        graph.ajouter_arete(a[0], a[1], a[2])

def sommetdmin(v, d) :
    '''Recherche le sommet le plus proche à partir d'une table de distance
    Parametres : v -> sommets atteignables
                d -> table des distances
    Retour : Noeud le plus proche (type : 'str)
    '''
    dmin = min([d[i][0] for i in v])
    for i in v :
        if d[i][0] == dmin : return i
    
def dijkstra(graph, start) :
    ''' Construit la table des distances en suivant l'algorithme de Dijkstra
    Parametres  -> graph : graphe (type : Graphe_pondere)
                -> strat : noeud départ (type str)
    Retour : table des distances (type : dict)
    '''
    lst_e = [] # Liste des sommets explores
    lst_v = [start] # liste des sommets atteignables
    table_dist = {sommet : [float('inf'), None] for sommet in graph.sommets()}  # Table des distances
    table_dist[start][0] = 0
    sommet = start
    distance = 0
    while len(lst_v) > 0 :
        s1 = sommetdmin(lst_v, table_dist)
        lst_v.remove(s1)
        lst_e.append(s1)
        for s2 in graph.voisins(s1) :
            if s2 not in lst_e :
                lst_v.append(s2)
                if table_dist[s2][0] > table_dist[s1][0] + graph.poids(s1, s2) :
                    table_dist[s2] = [table_dist[s1][0] + graph.poids(s1, s2), s1]
    return table_dist


def chemin(table_distance, start, end) :
    '''renvoie le chemin le plus court
    Parametres : table_distances -> dictionnaire des distances entre le noeud et le noeud de depart
                    start -> Noeud de depart
                    end -> Noeud d'arrivee
    Retour : liste des noeuds constituant le chemin
    
    Test :
    >>> chemin({'R1': [0, None], 'R2': [0.1, 'R1'], 'R3': [0.2, 'R2'], 'R5': [0.30000000000000004, 'R3'], 'R4': [0.4, 'R5'], 'R6': [0.5, 'R4'], 'R7': [1.5, 'R6']}, 'R1','R7')
    ['R7', 'R6', 'R4', 'R5', 'R3', 'R2', 'R1']
    '''
    chemin = [end]
    noeud = end
    while noeud != start :
        noeud = table_distance[noeud][1]
        chemin.append(noeud)
    return chemin
                    

# Definition du graphe de reference
aretes = [('R1','R2',0.1), ('R1','R3',1), ('R2','R3',0.1), ('R3','R5',0.1), ('R2','R4',1), ('R4','R5',0.1), \
          ('R4','R6',0.1), ('R5','R7',10), ('R5','R6',1), ('R6','R7',1)]

network = Graphe_pondere()
charger_aretes(network,aretes)