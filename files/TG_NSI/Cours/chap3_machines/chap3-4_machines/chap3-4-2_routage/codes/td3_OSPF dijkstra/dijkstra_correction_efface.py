from Graphe_pondere_correction import *

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
                if s2 not in lst_v : lst_v.append(s2)
                if table_dist[s2][0] > table_dist[s1][0] + graph.poids(s1, s2) :
                    table_dist[s2] = [table_dist[s1][0] + graph.poids(s1, s2), s1]
        print( 'v : ', lst_v, ' | e : ', lst_e, ' | s1 : ', s1, ' | dist : ', table_dist) 
        print('----------------------------------------------------')
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
    chemin.reverse()
    return chemin
                    

# Definition du graphe de reference
aretes = [('R1','R2',100), ('R1','R3',10), ('R2','R3',1), ('R3','R4',1), ('R2','R4',10), ('R2','R5',1), \
          ('R4','R5',1), ('R2','R6',1), ('R4','R6',10), ('R5','R6',1)]

network = Graphe_pondere()
charger_aretes(network,aretes)