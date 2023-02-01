import multiprocessing
import random
import time

def decoupe(l1):
    '''Decoupe une liste l1 en deux parties egales
    par utilisation de slices '''
    milieu = len(l1)//2
    return l1[:milieu], l1[milieu:]

def fusion(l1, l2) :
    '''Fusionne 2 listes triees l1 et l2'''
    l = []
    while len(l1)>0 and len(l2) :
        if l1[0] > l2[0] : l.append(l2.pop(0))
        else : l.append(l1.pop(0))
    return l + l1 + l2

def tri_fusion(l) :
    '''Trie la liste l par la methode tri par fusion'''
    l1, l2 = decoupe(l)
    if len(l1) > 1 : l1 = tri_fusion(l1)
    if len(l2) > 1 : l2 = tri_fusion(l2)
    return fusion(l1,l2)

def tri_fusion_parallele(data) :
    '''tri fusion execute sur plusieurs taches paralleles
    data : liste d'entiers melanges
    '''
    nb_proc =  ######### A completer ###################
    np =  ######### A completer ###################
    tdata = [data[i*np:(i+1)*np] for i in range(nb_proc)]
    pool = multiprocessing.Pool(processes=nb_proc)
    pdata = pool.map(tri_fusion,tdata)
    return fusion_taches(pdata)

def fusion_taches(pdata) :
    ''' fusionne les listes triees par les processus'''
    file = list(pdata)
    while len(file) > 1 :
        l1 = file.pop(0)
        l2 = file.pop(0)
        file.append(fusion(l1, l2))
    return file[0]

def fusion_taches_parallele(pdata, pool) :
    '''Fusionne plusieurs listes avec des taches paralleles)'''
    while len(pdata)>1 :
        extra = pdata.pop() if len(pdata)%2 == 1 else None
        paires = [(pdata[i], pdata[i+1]) for i in range(0, len(pdata), 2)]
        pdata = pool.starmap(fusion, paires)+([extra]if extra  else [])
    return pdata

def performance() :
    ''' Tri fusion : Comparaison des performances lors de l'utilisation de taches paralleles'''
    size = 2**18  # Taille des donnes à trier
    a_trier = [random.randint(0,size) for _ in range(size)]
    for tri in tri_fusion, tri_fusion_parallele :
        random.shuffle(a_trier)
        t0 = time.time()
        res = tri(a_trier)        
        t = time.time() - t0
        print(tri.__name__, t)

