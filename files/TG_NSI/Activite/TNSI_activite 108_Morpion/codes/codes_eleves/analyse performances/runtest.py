import time
from MorpionIA import *
import copy

def performance_IA_memo():
    '''Affiche les performances temps/espace de l'algorithme de backtracking avec memoisation
    Plateau 9 et 12 cases
    '''
    resultat = {'nbre_cases' : [], 't_minmax_memo':[], 'mem_minmax_memo' : []}
    for i in [9,12] :
        print('Test pour plateau de ',i, ' cases')
        resultat['nbre_cases'].append(i)
        m = MorpionIA(i)
        t0 = time.time()
        m.minmax_memo('x')
        resultat['t_minmax_memo'].append(time.time() - t0)
        resultat['mem_minmax_memo'].append(len(m.memo))

    rapport_memo(resultat)


def compare_performances() :
    '''Compare les performances de l'algorithme de backtracking avec/sans memoisation
    Plateau 9 cases et copus restants variant de 3 à 9 (plateau vide)
    '''
    resultat = {'nbre_coups' : [], 't_minmax' : [], 't_minmax_memo':[], 'mem_minmax' :[] , 'mem_minmax_memo' : []}
    for i in range(3,10) :
        print('Test pour nombre de coups restants = ',i)
        resultat['nbre_coups'].append(i)
        m = init_Morpion(9-i)
        t0 = time.time()
        m.minmax('x')
        resultat['t_minmax'].append(time.time() - t0)
        resultat['mem_minmax'].append(len(m.memo))
        m = init_Morpion(9-i)
        t0 = time.time()
        m.minmax_memo('x')
        resultat['t_minmax_memo'].append(time.time() - t0)
        resultat['mem_minmax_memo'].append(len(m.memo))
        rapport(resultat)

def rapport(result) :
    '''Affiche le rapport de test'''
    print('                                                                        ')
    print('                                                                        ')
    print('************************************************************************')
    print('******************** Rapport de performance ****************************')
    print('************************************************************************')
    print('Conditions : |Plateau 9 cases                                           ')
    print('             |Nombres de coups restants variant de 3 à 9 (plateau vide) ')
    print('                                                                        ')
    print('------------------------------------------------------------------------')
    print('Nombre de coups |temps execution sans memo  |temps execution avec memo |')
    print('------------------------------------------------------------------------')
    for i in range (len(result['nbre_coups'])):
        print(' '*((17-len(result['nbre_coups']))//2), end='')
        print(str(result['nbre_coups'][i]), end='')
        print(' '*(17-len(result['nbre_coups'])), end='|')
        print((str(result['t_minmax'][i])+' '*26)[:27],end='|')
        print((str(result['t_minmax_memo'][i])+' '*26)[:26],end='|')
        print()

def rapport_memo(result) :
    '''Affiche le rapport de test de la solution avec memoisation'''
    print('                                                                        ')
    print('                                                                        ')
    print('************************************************************************')
    print('******************** Rapport de performance ****************************')
    print('************************************************************************')
    print('Conditions : |Plateau 9 et 12 cases                                     ')
    print('             |Algorithme de backtracking avec memoisation               ')
    print('                                                                        ')
    print('------------------------------------------------------------------------')
    print('Nombre de cases |temps execution            |taille du dictionnaire    |')
    print('------------------------------------------------------------------------')
    for i in range (len(result['nbre_cases'])):
        print(' '*((12-len(result['nbre_cases']))//2), end='')
        print(str(result['nbre_cases'][i]), end='')
        print(' '*(12-len(result['nbre_cases'])), end='|')
        print((str(result['t_minmax_memo'][i])+' '*26)[:27],end='|')
        print((str(result['mem_minmax_memo'][i])+' '*26)[:26],end='|')
        print()

def init_Morpion(nbre_coups_joues : int) :
    '''Initialise un morpion avec Nbre_coups_joues joues sur le plateau'''
    m = MorpionIA()
    for i in range(nbre_coups_joues) :
        memoPlateau = copy.copy(m.getPlateau())
        for n in m.coupsRestants():
            m.jouer(m.tourDeJouer(),n)
            if not(m.analyserPlateau()[0]) :
                break
            else :
                m.setPlateau(memoPlateau)
    return  m






