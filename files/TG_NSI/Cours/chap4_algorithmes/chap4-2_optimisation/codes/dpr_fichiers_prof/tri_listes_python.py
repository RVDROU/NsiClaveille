# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:45:08 2020


Algorithmes de tri
"""



def tri_selection(lst):
    n = len(lst)
    for i in range(n):
        min = lst[i]
        pos_min = i
        for j in range(i+1, n):
            if lst[j] < min:
                min = lst[j]
                pos_min = j
        lst[i], lst[pos_min] = lst[pos_min], lst[i]
    return lst


def tri_insertion(lst):
    for i in range(1, len(lst)):
        e = lst[i]
        j = i
        while j > 0 and e < lst[j-1]:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = e
    return lst


# Tri fusion classique sur liste Python
# Cette version crée une nouvelle liste et ne modifie pas la liste de départ

def fusionne(lst1, lst2):
    """
    Example
    -------
    >>> fusionne([1, 3, 4, 7, 8], [2, 5, 6])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    
    res = []
    i = j = 0
    l1, l2 = len(lst1), len(lst2)
    while i < l1 and j < l2:
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    res = res + lst1[i:] + lst2[j:]	# une des deux listes ajoutées est vide
    return res

def tri_fusion(lst):
    "Tri fusion d'une liste Python"
    if len(lst) <= 1:
        return lst
    else:
        n = len(lst)//2
    return fusionne(tri_fusion(lst[:n]), tri_fusion(lst[n:]))



# Tri fusion version tableau
# proche de ce qui se fait dans d'autres langages (C, Java...)


def fusionne_tab(tab, deb, n, fin, tab_temp):
    """
    Fusionne deux parties d'un tableau

    Parameters
    ----------
    tab : list
        tableau contenant les listes à fusionner
    deb : int
        indice du premier élément de la première liste
    n : int
        indice du dernier élément de la première liste
    fin : int
        indice du dernier élément de la deuxième liste
        Le premier élément de la deuxième liste a pour indice n+1
    tab_temp : TYPE
        tableau temporaire de même taille que tab servant à stocker
        la liste fusionnée lors de sa construction, avant recopie dans tab

    Returns
    -------
    None.
   

    """
    i = deb
    j = n + 1
    k = deb
    while k <= fin:
        if i == n + 1:
            tab_temp[k] = tab[j]
            j += 1
        elif j == fin + 1:
            tab_temp[k] = tab[i]
            i += 1
        elif tab[i] < tab[j]:
            tab_temp[k] = tab[i]
            i += 1
        else:
            tab_temp[k] = tab[j]
            j += 1
        k += 1
    tab[deb:fin+1] = tab_temp[deb:fin+1]


def tri_fusion_tab(tab):
    "Tri fusion d'un tableau"
    # tab = tab[:] # décommenter pour éviter la modification du tableau de départ
    tab_temp = [0] * len(tab)
    def tri_fusion_(tab, deb, fin):
        """
        tri fusion de la partie du tableau allant de l'indice deb à 
        l'indice fin (inclus)'
        """
        if fin > deb:
            n = (deb + fin)//2
            tri_fusion_(tab, deb, n)
            tri_fusion_(tab, n+1, fin)
            fusionne_tab(tab, deb, n, fin, tab_temp)
    tri_fusion_(tab, 0, len(tab)-1)
    return tab



# On peut aussi créer le tableau temporaire dans la fonction
# fusionne mais cela complique un peu le code :

def fusionne_tab_2(tab, deb, n, fin):
    tab_temp = [0] * (fin + 1 - deb)
    i = deb
    j = n + 1
    k = deb
    while k <= fin:
        if i == n + 1:
            tab_temp[k - deb] = tab[j]
            j += 1
        elif j == fin + 1:
            tab_temp[k - deb] = tab[i]
            i += 1
        elif tab[i] < tab[j]:
            tab_temp[k - deb] = tab[i]
            i += 1
        else:
            tab_temp[k - deb] = tab[j]
            j += 1
        k += 1
    tab[deb:fin+1] = tab_temp[:fin+1-deb]


def tri_fusion_tab_2(tab):
    # tab = tab[:] # décommenter pour éviter la modification du tableau de départ
    
    def tri_fusion_(tab, deb, fin):
        if fin > deb:
            n = (deb + fin)//2
            tri_fusion_(tab, deb, n)
            tri_fusion_(tab, n+1, fin)
            fusionne_tab_2(tab, deb, n, fin)
    tri_fusion_(tab, 0, len(tab)-1)
    return tab




