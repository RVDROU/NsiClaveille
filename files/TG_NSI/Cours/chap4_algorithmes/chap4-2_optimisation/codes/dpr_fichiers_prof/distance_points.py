# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:22:56 2020

@author: kourf
"""

import random
import doctest
import timeit
import matplotlib.pyplot as plt


def distance(p1, p2):
    """
    Renvoie la distance entre deux points

    
    Exemple
    -------
    >>> distance((1, 2), (3, 5))
    3.605551275463989
    """
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def plus_proches(points: list) -> (float, tuple, tuple): 
    """
    Recherche les deux points les plus proches d'une liste de points

    Parameters
    ----------
    points : list
        liste des points définis par leurs coordonnées 
        [(x1, y1), …, (xn, yn)] 

    Returns
    -------
    (float, tuple, tuple)
        la distance minmale et les deux points les plus proches

    
    Example
    -------
    >>> plus_proches([(3, 4), (2, -1), (0.5, 2), (3, -4), (-1, -0.5), (-2, 5)])
    (2.9154759474226504, (0.5, 2), (-1, -0.5))
    
    """
    n = len(points)
    i0, j0 = 0, 0
    dmin = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            if distance(points[i], points[j]) < dmin:
                dmin = distance(points[i], points[j])
                i0, j0 = i, j
    return dmin, points[i0], points[j0]



def plus_proches_dpr(points: list) -> (int, int, float): 
    """
    Même préconditions et postconditions que plus_proches
    Utilise la méthode diviser pour régner
    """
    def plus_proches_rec(Px: list, Py: list) -> (int, int, float): 
        # étape 2
        n = len(Px)
        if n <= 3:
            return plus_proches(Px)
        Ax = Px[:n//2]
        x = Px[n//2][0]
        Ay = [p for p in Py if p[0] < x]
        Bx = Px[n//2:]
        By = [p for p in Py if p[0] >= x]
        # étape 3
        dA, p1A, p2A = plus_proches_rec(Ax, Ay)
        dB, p1B, p2B = plus_proches_rec(Bx, By)
        (d, p1, p2) = min((dA, p1A, p2A), (dB, p1B, p2B))
        # étape 4
        Qy = [p for p in Py if x - d < p[0] < x + d]
        dmin = d+1
        i0, j0 = 0, 0
        for i in range(len(Qy)-1):
            for j in range(1, min(7, len(Qy)-i)):
                if distance(Qy[i], Qy[i+j]) < dmin:
                    dmin = distance(Qy[i], Qy[i+j])
                    i0, j0 = i, i+j
        d, p1, p2 = min((d, p1, p2), (dmin, Qy[i0], Qy[j0]))
        return d, p1, p2
       
    Px = sorted(points)
    Py = sorted(points, key=lambda p: p[1])
    return plus_proches_rec(Px, Py)
    
    

def test_alea(xmin, xmax, ymin, ymax, nb):
    """
    Génère aléatoirement une liste de nb points
    d'abscisses entre xmin et xmax et d'ordonnées entre ymin et ymax
    """
    res = []
    for i in range(nb):
        x = xmin + (xmax - xmin) * random.random()
        y = ymin + (ymax - ymin) * random.random()
        res.append((x, y))
    return res        


def test_plus_proches_dpr():
    # Validité
    tests = ([[(-74, 26), (-61, 47), (-62, 37), (-39, -82)]]
             + [test_alea(-100, 100, -100, 100, 10) for i in range(100)]
             + [test_alea(-100, 100, -100, 100, 201) for i in range(10)])
    for t in tests:
        res1 = plus_proches(t)
        res2 = plus_proches_dpr(t)
        if res1[0] != res2[0] or {res1[1], res1[2]} != {res2[1], res2[2]}:
            print('test failed on', t)
            print('got', res1, 'and', res2)
            return
    print('Validité ok')
    # Vitesse
    npoints = 1000
    nrepeat = 10
    print('Temps de calcul lors de {} recherches sur des nuages de {} points'.format(nrepeat, npoints))
    t1 = timeit.timeit('plus_proches(test_alea(-100, 100, -100, 100, {}))'.format(npoints), globals = globals(), number=nrepeat)
    t2 = timeit.timeit('plus_proches_dpr(test_alea(-100, 100, -100, 100, {}))'.format(npoints), globals = globals(), number=nrepeat)
    print('Recherche naïve : {} - Algorithme diviser pour régner : {}'.format(t1, t2))





def graphique_ppdpr(n):
    points = test_alea(-10, 10, -10, 10, n)
    absc = [p[0] for p in points]
    ordo = [p[1] for p in points]
    plt.scatter(absc, ordo, color='black')
    d, p1, p2 = plus_proches_dpr(points)
    #plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red')
    plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='red')
    plt.show()
    


def graphique_cours(n, box=False):
    if box:    
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_aspect('equal')
    d = 0
    while d < 1.5:
        points = test_alea(-10, 10, -10, 10, n)
        points.sort()
        A = points[:n//2]
        B = points[n//2:]
        iA, jA, dA = plus_proches(A)
        iB, jB, dB = plus_proches(B)
        d = min(dA, dB)
    absc = [p[0] for p in points]
    ordo = [p[1] for p in points]
    plt.scatter(absc, ordo, color='black')
    x = absc[n//2]
    plt.plot([x, x], [-10, 10], color='red')
    plt.plot([A[iA][0], A[jA][0]], [A[iA][1], A[jA][1]], color='red')
    plt.plot([B[iB][0], B[jB][0]], [B[iB][1], B[jB][1]], color='red')
    plt.scatter([A[iA][0], A[jA][0], B[iB][0], B[jB][0]],
                [A[iA][1], A[jA][1], B[iB][1], B[jB][1]], color='red')
    plt.plot([x-d, x-d], [-10, 10], color='blue')
    plt.plot([x+d, x+d], [-10, 10], color='blue')
    if box:
        Q = [p for p in points if x - d < p[0] < x + d]
        iQ, jQ, d2 = plus_proches(Q)
        if d2 > d:
            plt.clf()
            graphique_cours(n, box=True)
            return
        p, q = Q[iQ], Q[jQ]
        y = min(p[1], q[1])
        plt.plot([x-d, x+d], [y,y], color='blue')
        plt.plot([x-d, x+d], [y+d/2, y+d/2], color='blue')
        plt.plot([x-d, x+d], [y+d, y+d], color='blue')
        plt.plot([x-d/2, x-d/2], [y, y+d], color='blue')
        plt.plot([x+d/2, x+d/2], [y, y+d], color='blue')
    plt.show()
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()