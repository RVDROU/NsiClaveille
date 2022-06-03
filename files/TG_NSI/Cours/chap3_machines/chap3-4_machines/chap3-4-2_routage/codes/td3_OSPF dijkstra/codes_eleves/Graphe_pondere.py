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
       
    
    def poids(self,s1, s2) :
        '''Retourne le poids de l'arete entre s1 et s2 si elle existe. None sinon'''
       

def test_graphe() :
    ''' Test la methode graphe_pondere() en verifiant les resultats obtenus a partir d'un graphe de référence'''
    # Construction du graphe de reference
    network = Graphe_pondere()
    network.ajouter_arete('R1', 'R2', 0.1)
    network.ajouter_arete('R1', 'R3', 1)

    
    # Verification de la methode sommets() (test complet donné en exemple)
    assert sorted(network.sommets()) == ['R1', 'R2', 'R3'] , 'Erreur dans la liste des sommets'
    
    # Verification de la methode arc_existe -> 1 test vari et 1 test faux
    
    
    # Verification des voisins de R1 puis ceux de R2
    
    # Verification du poids des deux aretes
 
    
    print('Test fini sans erreur')
    
