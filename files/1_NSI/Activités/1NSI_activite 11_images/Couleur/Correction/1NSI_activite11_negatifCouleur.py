from manipulationImage import *				
		

#Affiche le negatif d'une image
img=ouvrirImage("imageCouleur.png")
hauteur=len(img)
largeur=len(img[0])
afficherImage(img)
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        for i in range(3):
            img[ligne][colonne][i]=255-img[ligne][colonne][i]
            
        
       
        
            
		
afficherImage(img)