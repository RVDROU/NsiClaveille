'''
Exercices pratiques du BAC à faire pendant les vacances - Correction inspirée du
travail de Dorian DUPRAT

Liste des exercices :
Sujet 3_Ex1 ; Sujet 4_Ex1 ; Sujet 9_Ex1 ; Sujet 29_Ex1 ; Sujet 1_Ex2 ; Sujet 2_Ex2 ; Sujet 5_Ex2 ; Sujet 7_Ex2
https://rvdrou.github.io/NsiClaveille/10_Annales_EP/EP2022/EP_NSI_2022/
'''

# SUJET 3 Exercice 1

def delta(tab):
    '''
    Renvoie le codage par différence du tableau tab entrée en paramètre.
    
    Exemples :
        >>> delta([1000, 800, 802, 1000, 1003])
        [1000, -200, 2, 198, 3]
        >>> delta([42])
        42
    '''
    result = []
    if len(tab) == 1:
        return tab[0]
    for i in range(len(tab)-1):
        if i == 0:
            result.append(tab[i])
        result.append(tab[i+1]-tab[i])
    return result


# SUJET 4 Exercice 1

def recherche(tab):
    '''Renvoie les couples d'entiers consécutifs dans la liste
    tab entrée en paramètre.
    
    Exemples :
        >>> recherche([1, 4, 3, 5])
        []
        >>> recherche([1, 4, 5, 3])
        [(4, 5)]
        >>> recherche([7, 1, 2, 5, 3, 4])
        [(1, 2), (3, 4)]
        >>> recherche([5, 1, 2, 3, 8, -5, -4, 7])
        [(1, 2), (2, 3), (-5, -4)]
    '''
    liste_couples = []
    for i in range(len(tab)-1):
        if tab[i]+1 == tab[i+1]:
            liste_couples.append((tab[i],tab[i+1]))
    return liste_couples


# SUJET 9 Exercice 1

def calcul(n):
    '''Renvoie la liste des valeurs de la suite en partant du
    nombre entier n entré en paramètre jusqu'à atteindre 1.
    
    Exemple :
        >>> calcul(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    '''
    valeurs = [n]
    u_n = n
    while u_n != 1:
        if u_n%2 == 0: # Si un est pair
            u_n = u_n//2
            valeurs.append(u_n)
        else: # Si un est impaire
            u_n = 3*u_n+1
            valeurs.append(u_n)
    return valeurs


# SUJET 29 Exercice 1

def fibonacci(n):
    '''Prend l'entier n > 0 entré en paramètre et renvoie
    l'élément d'indice n de la suite de Fibonacci.
    
    Exemples :
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(25)
        75025
        >>> fibonacci(45)
        1134903170
    '''
    i = 3
    u1 = 1
    u2 = 1
    u_n = 1
    while i <= n:
        u_n = u2 + u1
        u1 = u2
        u2 = u_n
        i += 1
    return u_n


# SUJET 1 Exercice 2

pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution,i)
    else :
        return rendu_glouton(arendre, solution, i+1)


# SUJET 2 Exercice 2

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C


# SUJET 5 Exercice 2

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v
    
    """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
    def getNom(self):
        if (self.Valeur > 1 and self.Valeur < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"
    
    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []
    
    """Remplit le paquet de cartes"""
    def remplir(self):
        for i in range(1,5):
            for j in range(1,14):
                nouvelle_carte = Carte(i,j)
                self.contenu.append(nouvelle_carte)
    
    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        return self.contenu[pos]


# SUJET 7 Exercice 2

def tri_bulles(T):
    n = len(T)
    for i in range(n-1,0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


# ---------------------------------------------------------------------------------------------------------



REPORT_FILE = "report.txt"
report = open(REPORT_FILE,"a")

try :
    assert(delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3])
    report.write('    - Test de la fonction "delta" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> La fonction delta n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> jeu de test 1 non validé\n''')
except :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> erreur \n''')
    
try :
    assert(delta([42]) == 42)
    report.write('    - Test de la fonction "delta" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> La fonction delta n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> jeu de test 2 non validé\n''')
except :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> erreur \n''')

try :
    assert(recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)])
    report.write('    - Test de la fonction "recherche" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "recherche" : NONVALIDE -> La fonction recherche n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "recherche" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "recherche" : NONVALIDE -> erreur \n''')

try :
    assert(calcul(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    report.write('    - Test de la fonction "calcul" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "calcul" : NONVALIDE -> La fonction calcul n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "calcul" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "calcul" : NONVALIDE -> erreur \n''')

try :
    assert(fibonacci(1) == 1)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 1 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 1 \n''')
    
try :
    assert(fibonacci(2) == 1)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 2 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 2 \n''')
    
try :
    assert(fibonacci(25) == 75025)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 3 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 3 \n''')

try :
    assert(fibonacci(45) == 1134903170)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 4 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 4 \n''')

try :
    assert(rendu_glouton(68,[],0) == [50, 10, 5, 2, 1])
    report.write('    - Test de la fonction "rendu_glouton" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> La fonction rendu_glouton n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> jeu de test 1 non validé\n ''')
except :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> erreur test 1 \n''')
    
try :
    assert(rendu_glouton(291,[],0) == [100, 100, 50, 20, 20, 1])
    report.write('    - Test de la fonction "rendu_glouton" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> La fonction rendu_glouton n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> jeu de test 2 non validé\n ''')
except :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> erreur test 2 \n''')


try :
    assert(pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    report.write('    - Test de la fonction "pascal" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "pascal" : NONVALIDE -> La fonction pascal n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "pascal" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "pascal" : NONVALIDE -> erreur \n''')


unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
try :
    assert(uneCarte.getNom() + " de " + uneCarte.getCouleur() == "8 de coeur")
    report.write('    - Test de la classe "PaquetDeCarte" : VALIDE\n')
except NameError :
    report.write('''    - Test de la classe "PaquetDeCarte" : NONVALIDE -> La classe "PaquetDeCarte" n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la classe "PaquetDeCarte" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la classe "PaquetDeCarte" : NONVALIDE -> erreur \n''')

try :
    assert(tri_bulles([8,36,15,73,94,25]) == [8,15,25,36,73,94])
    report.write('    - Test de la fonction "tri_bulles" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "tri_bulles" : NONVALIDE -> La fonction "tri_bulles" n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "tri_bulles" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "tri_bulles" : NONVALIDE -> erreur \n''')
    
report.write('\n')
report.close()


