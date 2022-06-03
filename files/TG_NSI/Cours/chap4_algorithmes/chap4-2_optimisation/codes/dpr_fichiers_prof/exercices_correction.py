# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:46:34 2020

@author: kourf
"""


def min_et_max(T):
    def min_et_max_(T, a, b):
        if b == a + 1:
            return (T[a], T[a])
        elif b == a + 2:
            if T[a] < T[a + 1]: 
                return (T[a], T[a + 1])
            else:
                return (T[a + 1], T[a])
        else:
            c = (a + b)//2
            min1, max1 = min_et_max_(T, a, c)
            min2, max2 = min_et_max_(T, c, b)
            return min(min1, min2), max(max1, max2)   

    return min_et_max_(T, 0, len(T))


'''
Version comptant le nombre de comparaisons

cp = [0]

def min_et_max(T):
    def min_et_max_(T, a, b):
        if b == a + 1:
            return (T[a], T[a])
        elif b == a + 2:
            cp[0] += 1
            if T[a] < T[a + 1]: 
                return (T[a], T[a + 1])
            else:
                return (T[a + 1], T[a])
        else:
            c = (a + b)//2
            min1, max1 = min_et_max_(T, a, c)
            min2, max2 = min_et_max_(T, c, b)
            cp[0] += 2
            return min(min1, min2), max(max1, max2)   

    return min_et_max_(T, 0, len(T)), cp
'''    
        
def tranche(tab):
    n = len(tab)
    smax = tab[0]
    imax = jmax = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += tab[j]
            if s > smax:
                smax = s
                imax = i
                jmax = j
    return tab[imax:jmax+1]
        
def tranche_mod(tab):
    n = len(tab)
    smax = tab[0]
    imax = jmax = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += tab[j]
            if s == smax and j - i < jmax - imax:
                smax = s
                imax = i
                jmax = j
            if s > smax:
                smax = s
                imax = i
                jmax = j
    return tab[imax:jmax+1]

def tranche_dpr(tab):
    def tranche_dpr_(tab, a, b):
        if b == a + 1:
            return tab[a], tab[a:a+1]
        elif b == a + 2:
            return max((tab[a], tab[a:a+1]),
                       (tab[a+1], tab[a+1:a+2]),
                       (tab[a] + tab[a+1], tab[a:a+2]))
        else:
            c = (a + b)//2
            s1, t1 = tranche_dpr_(tab, a, c)
            s2, t2 = tranche_dpr_(tab, c, b)
            smax, tmax = max((s1, t1), (s2, t2))
            simax = tab[c - 1]
            imax = c - 1
            s = 0
            for i in range(c-1, a-1, -1):
                s += tab[i]
                if s > simax:
                    simax = s
                    imax = i
            sjmax = tab[c]
            jmax = c
            s = 0
            for j in range(c, b):
                s += tab[j]
                if s > sjmax:
                    sjmax = s
                    jmax = j
            return max((smax, tmax), (simax + sjmax, tab[imax:jmax+1]))
    
    return tranche_dpr_(tab, 0, len(tab))[1]



#################################################
#                                               #
#                   TESTS                       #
#                                               #
#################################################


import tabletest as tt
import copy


def check_validity_for_tranche(solvers, tests):
    """
    Vérifie que tous les solveurs trouvent les mêmes résultats sur les tests proposés
    Modifié pour tranche car le test échouait en comparant les tranches [0, 1] et [1] 
    qui ont la même somme
    """
    
    res = []
    message = ""
    tests_cop = copy.deepcopy(tests)
    for t in tests_cop:
        res.append(solvers[0](t))
    for s in solvers[1:]:
        tests_cop = copy.deepcopy(tests)
        for i in range(len(tests_cop)):
            if sum(s(tests_cop[i])) != sum(res[i]): # ligne modifiée
                message += "Test failed on {} with solvers {} and {}".format(tests[i], solvers[0].__name__, s.__name__) + "\n"
    if message == "":
        print("Validity tests successful" + "\n")
    else:
        print(message)


def test_tranche_dpr():
    for nb in (20, 500):    
        print()
        print("Test avec des listes de {} nombres".format(nb))
        tests = tt.random_tests(-1000, 1000, nb, 100)
        check_validity_for_tranche([tranche, tranche_dpr], tests)
        tt.run_performance([tranche, tranche_dpr], tests)
        











