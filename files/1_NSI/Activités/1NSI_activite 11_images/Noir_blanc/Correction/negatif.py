from manipulationImage import * 

#Affiche le negatif d'une image
img=ouvrirImage("nb.png")
afficherImage(img)
hauteur=len(img)
largeur=len(img[0])
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        img[ligne][colonne] = 255 - img[ligne][colonne]
           

afficherImage(img)