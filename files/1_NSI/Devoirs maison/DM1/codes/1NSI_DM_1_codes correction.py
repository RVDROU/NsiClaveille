from random import randint


def devine_nombre() :
    print('devine le nombre !')
    nbre = randint(0, 100)
    reponse = -1
    while reponse != nbre :
        reponse = int(input())
        if reponse  > nbre : print('plus petit')
        else : print('plus grand')
    print("C'est gagné !")
    
def allumettes_ver1() :
    allumettes = 21
    
    while allumettes > 0 :
        print('Il y a', allumettes, 'allumettes')
        n_joueur = int(input('Combien en prenez vous ?'))
        allumettes -= n_joueur
        n_ordi = randint(1,3)
        print('Je prends', n_ordi,'allumettes')
        allumettes-= n_ordi
        
def allumettes_ver2() :
    allumettes = 21
    joueur = False # False : ordi / True : joueur
    
    while allumettes > 0 :
        print('Il y a', allumettes, 'allumettes')
        if joueur :            
            n_joueur = int(input('Combien en prenez vous ?'))
            allumettes -= n_joueur
            joueur = False
        else :
            n_ordi = randint(1,3)
            print('Je prends', n_ordi,'allumettes')
            allumettes-= n_ordi
            joueur = True
    if joueur : print('Vous avez perdu !')
    else : print('Vous avez gagne !')

def allumettes_ver3() :
    allumettes = 21
    joueur = False # False : ordi / True : joueur
    
    while allumettes > 0 :
        if joueur :
            print('Il y a', allumettes, 'allumettes')
            n_joueur = int(input('Combien en prenez vous ?'))
            if 1<=n_joueur<=3 :
                allumettes -= n_joueur
                joueur = False
            else : print('Il faut prendre entre 1 et 3 allumettes, recommencez!')
            
        else :
            n_ordi = allumettes + 1
            while n_ordi > allumettes :
                n_ordi = randint(1,3)
          
            print('Je prends', n_ordi,'allumettes')
            allumettes-= n_ordi
            joueur = True
            
            
    if joueur : print('Vous avez perdu !')
    else : print('Vous avez gagne !')    
        
def allumettes_ver4() :
    ''' Strategie gagnante : Il faut toujours laisser un nombre d'allumettes correspondant
    à un multiple de 4  '''
    
    allumettes = 21
    joueur = True # False : ordi / True : joueur
    
    while allumettes > 0 :
        if joueur :
            print('Il y a', allumettes, 'allumettes')
            n_joueur = int(input('Combien en prenez vous ?'))
            if 1<=n_joueur<=3 :
                allumettes -= n_joueur
                joueur = False
            else : print('Il faut prendre entre 1 et 3 allumettes, recommencez!')
            
        else :
            n_ordi = allumettes % 4
            while n_ordi > allumettes :
                n_ordi = randint(1,3)
                print('recommencer')
           
            print('Je prends', n_ordi,'allumettes')
            allumettes-= n_ordi
            joueur = True
            
            
    if joueur : print('Vous avez perdu !')
    else : print('Vous avez gagne !')        