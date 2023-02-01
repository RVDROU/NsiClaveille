from manipulationImage import *

#Affiche le negatif d'une image
img = ouvrirImage("image_cachee.pgm")
imgCachee = ouvrirImage("image_cachee.pgm")
afficherImage(img)
hauteur=len(img)
largeur=len(img[0])
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        for teinte in range(3) :
            imgCachee[ligne][colonne][teinte]=(img[ligne][colonne][teinte]&7)<<5

afficherImage(imgCachee)
