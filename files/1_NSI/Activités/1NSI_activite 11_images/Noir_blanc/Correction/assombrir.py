from manipulationImage import *				
		

#Affiche le negatif d'une image
img=ouvrirImage("nb.png")
hauteur=len(img)
largeur=len(img[0])
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        img[ligne][colonne]-=30
        if img[ligne][colonne]<0:
            img[ligne][colonne]=0
        
            
		
afficherImage(img)