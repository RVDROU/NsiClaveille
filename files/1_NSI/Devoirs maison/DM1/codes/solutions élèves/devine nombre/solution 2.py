from random import randint
nbre_aleatoire= randint(0,100)

def devine_le_nbr(a):
    while True:
        a= int(input("Devine le nombre"))
        
        if a<nbre_aleatoire:
            print("plus grand")
            
        else:
            print("plus petit")
            
        if a==nbre_aleatoire:
            print("Bravo vous avez gagné !")
    