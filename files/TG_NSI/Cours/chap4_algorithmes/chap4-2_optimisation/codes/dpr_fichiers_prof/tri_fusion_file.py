# -*- coding: utf-8 -*-
"""
Implémentation fonctionnelle des files
"""

def file_vide():
    return None

def enfiler(valeur, file):
    if est_vide(file):
        return (valeur, file_vide())
    return (file[0], enfiler(valeur, file[1]))

def defiler(file):
    return (file[0], file[1])

def est_vide(pile):
    return pile == None



"""
Tri fusion
"""

def fusionne(file1, file2):
    nfile = file_vide()
    while not est_vide(file1) or not est_vide(file2):
        if est_vide(file2): 
            val, file1 = defiler(file1)
        elif est_vide(file1):
            val, file2 = defiler(file2)
        elif defiler(file1)[0] < defiler(file2)[0]:
            val, file1 = defiler(file1)
        else:
            val, file2 = defiler(file2)
        nfile = enfiler(val, nfile)
    return nfile

def tri_fusion(file):
    if est_vide(defiler(file)[1]): # si la file est de longueur 1
        return file
    else:
        file1 = file_vide()
        file2 = file_vide()
        file_active = 1
        while not est_vide(file):
            valeur, file = defiler(file)
            if file_active == 1:
                file1 = enfiler(valeur, file1)
                file_active = 2
            else:
                file2 = enfiler(valeur, file2)
                file_active = 1
        return fusionne(tri_fusion(file1), tri_fusion(file2))
    

if __name__ == '__main__':
    file = enfiler(1, enfiler(2, enfiler(5, enfiler(7, enfiler(
                    4, enfiler(8, enfiler(3, file_vide())))))))
    
