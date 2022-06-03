import multiprocessing
import random
import time
from file import File

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

def fusion_taches_parallele(pdata, pool) :
    while len(pdata)>1 :
        extra = pdata.pop() if len(pdata) % 2 == 1 else None
        paires = [(pdata[i], pdata[i+1]) for i in range(0, len(pdata), 2)]
        pdata = pool.starmap(fusion, paires)+([extra] if extra  else [])
    return pdata

def tri_fusion_parallele(data) :
    '''tri fusion execute sur plusieurs taches paralleles
    lst : liste d'entiers melanges
    '''
    nb_proc = multiprocessing.cpu_count()
    np = len(data) // nb_proc
    tdata = [data[i*np:(i+1)*np] for i in range(nb_proc)]

    tdata = [data[i*np:(i+1)*np] if i < nb_proc - 1 else data[i*np:] for i in range(nb_proc)]



    pool = multiprocessing.Pool(processes = nb_proc)
    pdata = pool.map(tri_fusion,tdata)
    return fusion_multiple(pdata)

def fusion_multiple(pdata) :
    file = File()
    for e in pdata : file.enfiler(e)
    while file.nb_elements() > 1 :
        file.enfiler(fusion(file.defiler(), file.defiler()))
    return file.defiler()

def performance() :
    for i in range(8,19) :
        size = 2**i
        a_trier = [random.randint(0,size) for _ in range(size)]
        for tri in tri_fusion, tri_fusion_parallele :
            random.shuffle(a_trier)
            t0 = time.time()
            res = tri(a_trier)
            t = time.time() - t0
            print('[2**',i,']',tri.__name__,' :', t)

if __name__ == "__main__":
    performance()