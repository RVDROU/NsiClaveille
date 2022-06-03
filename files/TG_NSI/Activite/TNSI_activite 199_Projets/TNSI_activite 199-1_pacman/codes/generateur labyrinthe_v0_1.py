from numpy.random import randint
import matplotlib.pyplot as plt
import copy


class Pile :
    '''classe Pile '''
    def __init__(self) :
        self.__pile = []
    
    def __repr__(self) :
        return self.__pile.__repr__()
    
    def vide(self) :
        ''' Pile est vide (booleen'''
        return len(self.__pile) == 0
    
    def empile(self, v) :
        '''Empile v sur la pile'''
        self.__pile.append(v)
    
    def depile(self) :
        assert not(self.vide()), 'La pile est vide'
        return self.__pile.pop()

class File :
    '''classe Pile '''
    def __init__(self) :
        self.__file = []
    
    def __repr__(self) :
        return self.__file.__repr__()
    
    def vide(self) :
        ''' Pile est vide (booleen'''
        return len(self.__file) == 0
    
    def enfile(self, v) :
        '''Empile v sur la pile'''
        self.__file.append(v)
    
    def defile(self) :
        assert not(self.vide()), 'La pile est vide'
        return self.__file.pop(0)

def constructeur_table(val, dim) :
    ''' Createur d'un dictionneur ayant pour cle chaque case du labyrinthe. La valeur est entrée en parametre
    val : valeur à affecter à chaque nom de cellule
    dim : dimension du labyrinthe (tuple (l,h)
    retour : dictionnaire
    '''
    table = {}
    l, h = dim    
    for i in range(l) :
        for j in range(h) :
            if type(val) == type({}) or type(val) == type([]) or type(val) == type(()) :
                table[nom(i,j)] = copy.deepcopy(val)
            else :
                table[nom(i,j)] = val
    return table        

def nom(i,j) :
    return str(i)+'_'+str(j)

def taille(t) :
        l,h = 0,0
        for elem in t.keys() :
            elem = elem.split('_')
            if int(elem[0]) > l : l = int(elem[0])
            if int(elem[1]) > h : h = int(elem[1])
        return (l+1,h+1)

def labyrinthe(l : int, h : int) :
    '''Creation du labyrinthe.
    l, h : largeur, hauteur du labyrinthe
    Retour : labyrinthe represente sous forme de graphe (liste des successeurs)
    '''
    table = {}
    etat = {}
    pile = Pile()

    table = constructeur_table({'N': None, 'S' : None, 'E' : None, 'O' : None}, (l,h))
    etat = constructeur_table(False,(l,h))

    i, j = randint(l), randint(h)
    pile.empile((i,j))
    etat[nom(i,j)] = True
    while not pile.vide() :
        i, j = pile.depile()
        # Recherche des cases voisines disponibles
        voisins = []
        if j < h-1 and not etat[nom(i,j+1)] :
            voisins.append('N')
        if i > 0 and not etat[nom(i-1,j)] :
            voisins.append('O')
        if j > 0 and not etat[nom(i,j-1)] :
            voisins.append('S')
        if i < l-1 and not etat[nom(i+1,j)] :
            voisins.append('E')
        if len(voisins) > 1 :
            pile.empile((i,j))
        if len(voisins) > 0 :
            direction = voisins[randint(len(voisins))]
            if direction == 'N':
                table[nom(i,j)]['N'] = nom(i,j+1)
                table[nom(i,j+1)]['S'] = nom(i,j)
                etat[nom(i,j+1)] = True
                pile.empile((i,j+1))
            elif direction == 'O':
                table[nom(i,j)]['O'] = nom(i-1,j)
                table[nom(i-1,j)]['E'] = nom(i,j)
                etat[nom(i-1,j)] = True
                pile.empile((i-1,j))
            elif direction == 'S':
                table[nom(i,j)]['S'] = nom(i,j-1)
                table[nom(i,j-1)]['N'] = nom(i,j)
                etat[nom(i,j-1)] = True
                pile.empile((i,j-1))
            elif direction == 'E':
                table[nom(i,j)]['E'] = nom(i+1,j)
                table[nom(i+1,j)]['O'] = nom(i,j)
                etat[nom(i+1,j)] = True
                pile.empile((i+1,j))
            else : raise IndexError('index orientation inconnu')
    
    return table

def afficher(table):
    '''Affiche le labyrinthe'''      
    l,h = taille(table)
    plt.plot([0, 0, l, l, 0], [0, h, h, 0, 0], linewidth=2)
    for i in range(l-1):
        for j in range(h):
            if table[nom(i,j)]['E'] == None:
                plt.plot([i+1, i+1], [j, j+1], 'b')
    for j in range(h-1):
        for i in range(l):
            if table[nom(i,j)]['N'] == None:
                plt.plot([i, i+1], [j+1, j+1], 'b')
    plt.axis([-1, l+1, -1, h+1])
    plt.show()
    
def parcours_profondeur(laby) :
    '''Recherche la sortie avec un parcours en profondeur'''
    p = Pile()
    actuelle='0_0'
    l,h = taille(laby)
    sortie = str(l-1) + '_' + str(h-1)
    etat = constructeur_table(False,(l, h))
    while actuelle != sortie :
        etat[actuelle] = True
        voisins = [elem for elem in laby[actuelle].values() if elem != None and not(etat[elem])]
        if len(voisins) > 0 :
            p.empile(actuelle)
            for each in voisins :
                if not(etat[each]) :
                    p.empile(each)
        else :
            p.depile()
        assert not(p.vide()), 'Pile vide'
        actuelle = p.depile()
    return p
     
                
def algo_lee(laby) :
    '''Parcours en largeur numéroté'''
    chemin = []
    f = File()
    actuelle = '0_0'
    l,h = taille(laby)
    sortie = str(l-1) + '_' + str(h-1)
    etiquette = constructeur_table(None,(l, h))
    etiquette[actuelle]=0
    while actuelle != sortie :
        voisins = [elem for elem in laby[actuelle].values() if elem != None and etiquette[elem]==None]
        for each in voisins :
            etiquette[each] = etiquette[actuelle]+1
            f.enfile(each)
        actuelle = f.defile()
    
    num = etiquette[sortie]
    chemin.append(sortie)    
    while num != 0 :
        for cle, valeur in etiquette.items() :
            if valeur == num - 1:
                num = valeur
                chemin.append(cle)
    return chemin


    
def recherche_droite(laby) :
    '''Recherche le chemin de sortie en choisissant la routeà droite'''
    a_droite_de = {'N' : 'E', 'E' : 'S', 'S' : 'O', 'O' : 'N'}
    a_gauche_de = {'N' : 'O', 'O' : 'S', 'S' : 'E', 'E' : 'N'}
    direction = 'E'
    chemin = Pile()
    actuelle = '0_0'
    precedente = None
    prochain = None
    l,h = taille(laby)
    sortie = str(l-1) + '_' + str(h-1)
    chemin.empile(actuelle)
    while actuelle != sortie :
        print(actuelle, ' -> ', direction)
        if laby[actuelle][a_droite_de[direction]] != None :
            prochain = laby[actuelle][a_droite_de[direction]]
            precedent = chemin.depile()
            if prochain != precedent :
                chemin.empile(precedent)
                chemin.empile(actuelle)
            actuelle = prochain
            direction = a_droite_de[direction]
        else : direction = a_gauche_de[direction]
    return chemin
        
l = labyrinthe(5,5)

    
