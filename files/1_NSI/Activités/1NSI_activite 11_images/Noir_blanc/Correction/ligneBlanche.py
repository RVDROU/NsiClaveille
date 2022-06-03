from manipulationImage import *

#Affiche le negatif d'une image
img=ouvrirImage("nb.png")
hauteur=len(img)
largeur=len(img[0])
for ligne in range(int((hauteur/2))-10,int((hauteur/2))+10) :
    for colonne in range(largeur) :
        img[ligne][colonne]=255
        
            
		
afficherImage(img)