from random import randint
def choix_adverse(choix_input):
    '''permet a l'ordinateur de choisir le nombre d'allumettes
    qu'il retire en fonction du nombre d'allumettes que vient de
    retirer l'utilisateur.
    '''
    if choix_input==1:
        return(3)
    elif choix_input==2:
        return(2)
    else:
        return(1)

def choix_utilisateur():
    '''demande au joueur de saisir une valeur comprise entre
    1 et 3. si ce n'est pas le cas, un message apparait pour
    lui demander de choisir un nombre correcte et il repose
    la question.
    '''
    validation=0
    while validation==0:
        choix_input=int(input("Combien en prenez vous ?"))
        if 1<=choix_input<=3:
            validation=1
        else:
            print("veuillez saisir une valeur comprise entre 1 et 3")
    return(choix_input)


allumettes=21
choix_ordi=0
choix_input=0
while allumettes!=0:
    print("il y a",allumettes,"allumette(s)")
    choix_input=choix_utilisateur()
    allumettes=allumettes-choix_input
    if allumettes==1:
        print("vous avez gagne")
        allumettes=0
    else:
        choix_ordi=choix_adverse(choix_input)
        print("je prends",choix_ordi,"allumette(s)")
        allumettes=allumettes-choix_ordi
        if allumettes==1:
            print("vous avez perdu")
            allumettes=0
