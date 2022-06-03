import time
from MorpionIA import *

def compare_performances() :
    '''Compare les performances de l'algorithme de backtracking avec/sans memoisation
    Parametres : morpion : objet morpionIA
                v (int) : nombre de coups restants
    '''
    resultat = {'nbre_coups' : [], 't_minmax' : [], 't_minmax_memo':[], 'mem_minmax' :[] , 'mem_minmax_memo' : []}
    for i in range(9,10) :
        print('Test pour nombre de coups restants = ',i)
        resultat['nbre_coups'].append(i)
        m = MorpionIA()
        t0 = time.time()
        m.minmax('x')
        resultat['t_minmax'].append(time.time() - t0)
        resultat['mem_minmax'].append(len(m.memo))
        m = MorpionIA()
        t0 = time.time()
        m.minmax_memo('x')
        resultat['t_minmax_memo'].append(time.time() - t0)
        resultat['mem_minmax_memo'].append(len(m.memo))
        rapport(resultat)

def rapport(result) :
    print('************************************************************************')
    print('******************** Rapport de performance ****************************')
    print('************************************************************************')
    print('                                                                        ')
    print('                                                                        ')
    print('------------------------------------------------------------------------')
    print(' Nombre de coups |      temps sans memo     |      temps avec memo     |')
    print('------------------------------------------------------------------------')
    for i in range (len(result['nbre_coups'])):
        print(' '*((17-len(result['nbre_coups']))//2), end='')
        print(str(result['nbre_coups'][i]), end='')
        print(' '*(17-(17-len(result['nbre_coups'])//2)-len(result['nbre_coups'])), end='|')
        print((str(result['t_minmax'][i])+' '*26)[:27],end='|')
        print((str(result['t_minmax_memo'][i])+' '*26)[:27],end='|')
        print()
                       
    


        
    
        
        