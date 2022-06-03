from manipulationImage import *				
		

#Affiche le negatif d'une image
img=ouvrirImage("imageCouleur.png")
masque=ouvrirImage("masque.png")
hauteur=len(img)
largeur=len(img[0])
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        if masque[ligne][colonne]<127:
            
            for i in range(3):
                img[ligne][colonne][i]=img[ligne][colonne][i]-50
                if img[ligne][colonne][i]<0:
                    img[ligne][colonne][i]=0
        else:
            for i in range(3):
                img[ligne][colonne][i]=img[ligne][colonne][i]+50
                if img[ligne][colonne][i]>255 :
                    img[ligne][colonne][i]=255
        
		
afficherImage(img)