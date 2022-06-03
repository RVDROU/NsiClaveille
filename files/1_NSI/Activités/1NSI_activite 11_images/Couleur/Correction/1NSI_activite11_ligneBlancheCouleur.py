from manipulationImage import *				
		

#Affiche le negatif d'une image
img=ouvrirImage("imageCouleur.png")
masque=ouvrirImage("masque.png")
hauteur=len(img)
largeur=len(img[0])
for ligne in range(int((hauteur/2))-10,int((hauteur/2))+10) :
    for colonne in range(largeur) :
        for i in range(3):
            img[ligne][colonne][i]=255
           
afficherImage(img)

