from manipulationImage import *

#Affiche image en noir et blanc
img=ouvrirImage("nb.png")
hauteur=len(img)
largeur=len(img[0])
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        if img[ligne][colonne]<127 :
            img[ligne][colonne]=0
        else :
            img[ligne][colonne]=255
             
		
afficherImage(img)