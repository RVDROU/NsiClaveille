import concurrent.futures
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

def fusion2(l1, l2) :
    '''Fusionne 2 listes triees l1 et l2'''
    l = []
    print(l1)
    print(l2)
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

def fusion_taches_parallele(pdata, pool) :
#     while len(pdata)>1 :
#         extra = pdata.pop() if len(list(pdata))%2 == 1 else None
    paires = [(pdata[i], pdata[i+1]) for i in range(0, len(pdata), 2)]
#         pdata = pool.map(fusion, *zip(*paires))+([extra]if extra  else [])
#     return list(pdata)[0]
    return pool.map(fusion, paires)
 



def tri_fusion_parallele(data) :
    '''tri fusion execute sur plusieurs taches paralleles
    lst : liste d'entiers melanges
    '''
    nb_proc = multiprocessing.cpu_count()*2
    np = len(data) // nb_proc
    data = [data[i*np:(i+1)*np] if i < nb_proc-1 else data[i*np:] for i in range(nb_proc)]
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=nb_proc)
    tdata = pool.map(tri_fusion,data)
    pdata = pool.map(fusion2, tdata.__next__(), tdata.__next__())
    return pdata, tdata
    #return fusion_taches_parallele(pdata,pool)

def fusion_taches(pdata) :
    file = list(pdata)
    while len(file) > 1 :
        l1 = file.pop(0)
        l2 = file.pop(0)
        file.append(fusion(l1, l2))
    return file[0]

def comparaison_tri() :
    size = 2**18
    a_trier = [random.randint(0,size) for _ in range(size)]
    res_attendu = sorted(a_trier)

    for tri in tri_fusion, tri_fusion_parallele :
        random.shuffle(a_trier)
        t0 = time.time()
        res = tri(a_trier)
        
        t = time.time() - t0
        print(res)
        print(tri.__name__, t)
        assert res == res_attendu
def load() :
    size = 2**8
    a_trier = [random.randint(0,size) for _ in range(size)]
    return tri_fusion_parallele(a_trier)