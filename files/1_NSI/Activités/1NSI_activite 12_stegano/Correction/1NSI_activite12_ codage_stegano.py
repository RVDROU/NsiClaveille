from manipulationImage import *				
		

#Affiche le negatif d'une image
imgSupport=ouvrirImage("pop.png")
imgACacher=ouvrirImage("mouton.png")
hauteur=len(imgSupport)
largeur=len(imgSupport[0])
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        for teinte in range(3) :
            imgSupport[ligne][colonne][teinte]=imgSupport[ligne][colonne][teinte]&248 | (imgACacher[ligne][colonne][teinte]>>5)&7

afficherImage(imgSupport)
