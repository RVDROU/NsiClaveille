# -*- coding: utf-8 -*-
"""
Module de tests pour le tp sur le tri fusion
"""

import doctest
import time
import random
import copy
import matplotlib.pyplot as plt
from tri_listes_python import *




def random_tests(lower, higher, len_lst, nb_tests):
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
        lst = [random.randint(lower, higher) for i in range(len_lst)]
        res.append(lst)
    return res
    
def almost_sorted_list(lower, len_lst, nb_permutations, nb_tests):
    """
    Le nombre de permutations n'est pas garanti car une permutation peut être 
    l'identité ou deux permutations peuvent se compenser.
    """
    res = []
    for i in range(nb_tests):
        lst = list(range(lower, lower + len_lst))
        for j in range(nb_permutations):
            a = random.randrange(len_lst)
            b = random.randrange(len_lst)
            lst[a], lst[b] = lst[b], lst[a]
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



def test_solvers(solvers, test_parameters = None):
    "Lance les tests de validité et de performance sur plusieurs jeux de tests"
    tests = almost_sorted_list(1, 1000, 10, 10)
    print('Tests on almost sorted lists of 1000 numbers (at worse 20 numbers not at the right position)')
    check_validity(solvers, tests)
    run_performance(solvers, tests)   
    print("Random tests")
    if test_parameters == None:
        test_parameters = ((0, 1000, 10, 10000),
                           (10000000, 99999999, 100, 100),
                           (0, 10000000, 1000, 10),
                           (100000, 999999, 1000, 10),
                           (1000000000, 9999999999, 2000, 1),
                           (10000, 99999, 5000, 1),
                           )
    for lower, higher, len_lst, nb_tests in test_parameters:
        tests = random_tests(lower, higher, len_lst, nb_tests)
        print("""\nsmallest value : {}, highest value : {}, list length : {}, number of tests : {},
                                  \n""".format(lower, higher, len_lst, nb_tests)) 
        check_validity(solvers, tests)
        run_performance(solvers, tests)


def draw_performance(solvers, lmax):
    "Trace pour les différents solveurs la vitesse en fonction de n, longueur de la liste"
    tests = []
    absc = []
    times = []
    for length in range(100, lmax, 100):
        absc.append(length)
        tests.append(random_tests(0, 10000, length, 1)[0])
    for s in solvers:
        tests_cop = copy.deepcopy(tests)
        time_solv = []
        for t in tests_cop:
            start_time = time.time()
            s(t)
            end_time = time.time()
            time_solv.append(end_time - start_time)
        times.append(time_solv)    
    for i in range(len(solvers)):
        plt.plot(absc, times[i], label=solvers[i].__name__)
    plt.legend()
    plt.show()


def test_fusionne():
    doctest.run_docstring_examples(fusionne, globals(), verbose=True)

def test_tri_fusion():
    tests = random_tests(0, 1000, 50, 100)
    check_validity([tri_selection, tri_fusion], tests)

def test_sorts():
    test_solvers([tri_selection, tri_insertion, tri_fusion])

def compare_tris():
    draw_performance([tri_selection, tri_insertion, tri_fusion], 2000)


def test_fusionne_tab():
    for tab, deb, n, fin, exp, len_temp in  (([1, 3, 4, 7, 8, 2, 5, 6], 0, 4, 7, [1, 2, 3, 4, 5, 6, 7, 8], 8), 
                                             ([1, 3, 4, 8, 0, 2, 5, 6, 7], 0, 3, 8, [0, 1, 2, 3, 4, 5, 6, 7, 8], 9)):
        print('Testing fusionne_tab({}, {}, {}, {}, [0]*{})'.format(tab, deb, n, fin, len_temp))
        print('Expecting : ', exp)
        fusionne_tab(tab, deb, n, fin, [0]*len_temp)
        if tab == exp:
            print('ok')
        else:
            print('Got : ', tab)
            print('Test failed')
  
def test_tri_fusion_tab():
    tests = random_tests(0, 1000, 50, 100)
    check_validity([tri_fusion, tri_fusion_tab], tests)        

def compare_tris_fusion():
    draw_performance([tri_fusion_tab, tri_fusion_tab_2, tri_fusion], 5000)

