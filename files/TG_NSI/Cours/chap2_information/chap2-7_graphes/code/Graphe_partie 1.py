#import networkx as nx
import matplotlib.pyplot as plt

class Graphe :
    '''Graphe represente par sa matrice d'adjacence,
    où les sommets sont les entiers o, 1, ..., n-1'''
    
    def __init__(self, n) :
        self.__n = n
        self.__adj = [[False] * n for _ in range(n)]
    
    def __repr__(self) :
        txt =''
        bit = {False : '0', True : '1'}
        for i in self.__adj :
            txt = txt + '| '
            for j in i :
                txt = txt + bit[j] + ', '
            txt = txt[:-2] + ' |' + '\n'
        return txt

    def ajouter_arete(self, s1, s2) :
        '''Ajoute un arc entre les sommets s1 et S2'''
        self.__adj[s1][s2] = True
        self.__adj[s2][s1] = True
    
    def supprimer_arete(self, s1, s2) :
        '''Ajoute un arc entre les sommets s1 et S2'''
        self.__adj[s1][s2] = False
        self.__adj[s2][s1] = False
        
    def arete(self, s1, s2) :
        '''Indique la presence d'un arc ou non
        entre s1 et s2'''
        return self.__adj[s1][s2]
    
    def voisins(self, s) :
        '''Renvoie la liste des voisins de s'''
        v =[]
        for i in range(self.__n) :
            if self.arete(i,s) :
                v.append(i)
        return v
    
    def degre(self,s) :
        '''Nombre d'arretes sur le sommet s'''
        return self.__adj[s].count(True)
    
    def nb_aretes(self) :
        ''' Nombre d'aretes dans le graphe'''
        n = 0
        for i in range(self.__n) :
            n+=self.degre(i)
        return n/2
    
    def matrix_to_list(self) :
        liste_succ = {}
        for i in range(len(self.__adj)) :
            liste_succ[i] = self.voisins(i)
        return liste_succ
    
    def afficher(self) :
        for i in range(self.__n):
            proches = self.voisins(i)
            print (i, ' -> ', end='')
            for p in proches :
                print (p, end =' ')
            print()
            
    def afficher_graphe(self) :
        n = len(self.__adj)
        G = nx.Graph()
        for l in range(n) :
            for c in range(n) :
                if self.__adj[l][c] :
                    G.add_edge(str(l),str(c))
                
        pos = nx.spring_layout(G)
        nx.draw(G, pos, font_size=16, with_labels=False)
        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
        plt.show()
    
   
            
                    
p={'Alban':0,'Béatrice':1, 'Charles':2, 'Déborah':3, 'Eric':4, 'Fatima':5, 'Gérald':6, 'Hélène':7}
g = Graphe(8)
g.ajouter_arete(p['Alban'],p['Béatrice'])
g.ajouter_arete(p['Alban'],p['Déborah'])
g.ajouter_arete(p['Alban'],p['Eric'])
g.ajouter_arete(p['Alban'],p['Fatima'])
g.ajouter_arete(p['Béatrice'],p['Charles'])
g.ajouter_arete(p['Béatrice'],p['Déborah'])
g.ajouter_arete(p['Béatrice'],p['Eric'])
g.ajouter_arete(p['Béatrice'],p['Gérald'])
g.ajouter_arete(p['Charles'],p['Déborah'])
g.ajouter_arete(p['Charles'],p['Hélène'])
g.ajouter_arete(p['Déborah'],p['Gérald'])
g.ajouter_arete(p['Fatima'],p['Gérald'])
g.ajouter_arete(p['Fatima'],p['Hélène'])
g.ajouter_arete(p['Gérald'],p['Hélène'])

#g.afficher_graphe()


