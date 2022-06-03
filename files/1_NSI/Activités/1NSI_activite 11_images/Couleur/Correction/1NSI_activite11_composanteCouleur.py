from manipulationImage import *				
		

#Affiche le negatif d'une image
img=ouvrirImage("imageCouleur.png")
hauteur=len(img)
largeur=len(img[0])
choix=int(input("Choix de composante : 1/rouge ; 2/vert ; 3/bleu"))
for ligne in range(hauteur) :
    for colonne in range(largeur) :
        if choix==1:
            img[ligne][colonne][1]=0
            img[ligne][colonne][2]=0
        elif choix==2:
            img[ligne][colonne][0]=0
            img[ligne][colonne][2]=0
        elif choix==3:
            img[ligne][colonne][0]=0
            img[ligne][colonne][1]=0
        else :
            print("choix incorrect")
        
       
        
            
		
afficherImage(img)