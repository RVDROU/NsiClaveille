# -*- coding: utf-8 -*-
"""
Module de tests pour les tableaux
"""

import time
import random
import copy



def random_tests(lower, higher, len_lst, nb_tests, integer=True):
    """
    
    Parameters
    ----------
    lower : int
        nombre le plus petit
    higher : int
        nombre le plus grand
    len_lst : int
        longueur de la liste
    nb_tests : int
        nombre de tests

    Returns
    -------
    res : list
        liste de listes de nombres entiers à trier

    """
        
    res = []
    for i in range(nb_tests):
        if integer==True:
            lst = [random.randint(lower, higher) for i in range(len_lst)]
        else:
            lst = [lower + random.random()*(higher - lower) for i in range(len_lst)]
        res.append(lst)
    return res
    



def check_validity(solvers, tests):
    "Vérifie que tous les solveurs trouvent les mêmes résultats sur les tests proposés"
    res = []
    message = ""
    tests_cop = copy.deepcopy(tests)
    for t in tests_cop:
        res.append(solvers[0](t))
    for s in solvers[1:]:
        tests_cop = copy.deepcopy(tests)
        for i in range(len(tests_cop)):
            if s(tests_cop[i]) != res[i]:
                message += "Test failed on {} with solvers {} and {}".format(tests[i], solvers[0].__name__, s.__name__) + "\n"
    if message == "":
        print("Validity tests successful" + "\n")
    else:
        print(message)
       

def run_performance(solvers, tests):
    "Compare la vitesse des différents solveurs sur les tests proposés"
    for s in solvers:
        tests_cop = copy.deepcopy(tests)
        start_time = time.time()
        for t in tests_cop:
            s(t)
        end_time = time.time()
        print("{} ran the tests in {} seconds".format(s.__name__, end_time - start_time))

