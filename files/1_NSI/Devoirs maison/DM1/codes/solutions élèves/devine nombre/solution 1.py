from random import randint

def devine_nombre():
    '''
    le joueur doit trouver le nombre mystère (entre 0 et 100) choisi au préalable par le maître du jeu, qui sera ici l’ordinateur. A chaque tour,
    le joueur propose un nombre et le maître de jeu, indique si le nombre mystère est plus petit ou plus grand que le nombre proposé.
    '''
    nbr_random = randint(0,100)
    essai=1
    nbr=int(input("Devine le nombre!"))
    while nbr!=nbr_random:
        essai=essai+1
        if nbr<nbr_random:
            nbr=int(input("Plus grand"))
        else:
            nbr=int(input("Plus petit"))
    else:
        print("Tu as trouvé, c'est", nbr,"en",essai,"essais")


