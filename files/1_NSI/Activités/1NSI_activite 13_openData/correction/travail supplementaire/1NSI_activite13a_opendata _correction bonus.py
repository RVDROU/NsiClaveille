import csv
from copy import deepcopy


def charger_table(fichier) :
    file = open(fichier)
    table = list(csv.DictReader(file,delimiter=";"))
    file.close()
    return table

def requete1() :
    basegardiens = charger_table('BaseGardiens.csv')
    extracted = []
    for elem in basegardiens :
        extracted.append(elem['NomAgent'])
    return extracted

def join(table1, table2, cle1, cle2) :
    t1 = deepcopy(table1)
    t2 = deepcopy(table2)
    fusion = []
    for elem1 in t1 :
        for elem2 in t2 :
            if elem1[cle1] == elem2[cle2] :
                base = deepcopy(elem1)
                del(base[cle1])
                base.update(elem2)
                fusion.append(base)
    return fusion

def requete2() :
    basegardiens = charger_table('BaseGardiens.csv')
    baseagents = charger_table('BaseAgents.csv')
    fusion = join(basegardiens, baseagents, 'NomAgent', 'NomAgent')
    result = []
    for elem in fusion :
        if elem['VilleAgent'] not in result :
            result.append(elem['VilleAgent'])
    return result

def requete3() :
    basealiens = charger_table('BaseAliens.csv')
    basecabines = charger_table('BaseCabines.csv')
    fusion = join(basealiens, basecabines, 'NoCabine', 'NoCabine')
    print(fusion)
    result = []
    for elem in fusion :
        if elem['NoAllee'] == '2' :
            result.append(elem['NomAlien'])
    return result

def requete4() :
    basealiens = charger_table('BaseAliens.csv')
    basegardiens = charger_table('BaseGardiens.csv')
    baseagents = charger_table('BaseAgents.csv')
    basevilles = charger_table('BaseVilles.csv')
      
    fusion = join(basealiens, basegardiens, 'NoCabine', 'NoCabine')
    fusion = join(fusion, baseagents, 'NomAgent', 'NomAgent')
    fusion = join(fusion, basevilles, 'VilleAgent', 'Ville')

    result = []
    for elem in fusion :
        if elem['Planete'] == 'Trantor' :
            result.append(elem['NomAgent'])
    return result

def requete5() :
    basemiams = charger_table('BaseMiams.csv')
    basealiens = charger_table('BaseAliens.csv')
    basegardiens = charger_table('BaseGardiens.csv')
      
    fusion = join(basealiens, basemiams, 'NomAlien', 'NomAlien')
    fusion = join(fusion, basegardiens, 'NoCabine', 'NoCabine')

    result = []
    for elem in fusion :
        if elem['Aliment'] == 'Bortsch' and  elem['Sexe'] == 'F' :
            result.append(elem['NomAgent'])
    return result

def test1() :
    basemiams = charger_table('BaseMiams.csv')
    basealiens = charger_table('BaseAliens.csv')
    basegardiens = charger_table('BaseGardiens.csv')
      
    fusion = join(basealiens, basemiams, 'NomAlien', 'NomAlien')
    fusion = join(fusion, basegardiens, 'NoCabine', 'NoCabine')

    result = []
    for elem in fusion :
        if elem['Aliment'][0] == elem['NomAgent'][0] :
            result.append((elem['NomAlien'], elem['NomAgent'],elem['Aliment']))
    return result


def test2() :
    basealiens = charger_table('BaseAliens.csv')
    basegardiens = charger_table('BaseGardiens.csv')
    baseagents = charger_table('BaseAgents.csv')
    basevilles = charger_table('BaseVilles.csv')
      
    fusion = join(basealiens, basegardiens, 'NoCabine', 'NoCabine')
    fusion = join(fusion, baseagents, 'NomAgent', 'NomAgent')
    fusion = join(fusion, basevilles, 'VilleAgent', 'Ville')

    result = []
    for elem in fusion :
        if 'x' in elem['NomAlien'].lower() and elem['Ville'] == 'Terminus' :
            result.append((elem['NomAlien'], elem['NomAgent']))
    return result
