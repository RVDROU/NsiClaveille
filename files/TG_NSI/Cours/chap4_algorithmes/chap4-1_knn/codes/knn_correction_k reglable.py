import csv
from math import sqrt

def extractionDonnees(nomFichier):
    '''Aide de la fonction distance du module knn :
    
    extractionDonnees(nomfihier)
        Extrait le jeu de donnees du fihier CSV et le met en forme
    
    ->Parametres : nomFichier : chaîne de caractère
                   
    -> Retour : liste des joueurs avec poste et gabarit -> liste de tuple au format : [('nom du joueur','poste du joueur','taille','masse')....]
    '''
    joueurs = []
    nomDuFichier = nomFichier
    if nomFichier[-4:]!=".csv":
        nomDuFichier+=".csv"
    fichier = open(nomDuFichier,"r",encoding="utf-8")
    descripteurs = fichier.readline()
    dialecte_fichier_csv = csv.Sniffer().sniff(descripteurs)
    data_lignes = list(csv.reader(fichier, dialect=dialecte_fichier_csv))
    for joueur in data_lignes :
        joueurs.append((joueur[1],joueur[3], joueur[5], joueur[6]))
    return joueurs

def distance(p1,p2):
    '''
    Aide de la fonction distance du module knn :
    
    distance(p1,p2)
        Calcule la distance Euclidienne separant deux points p1 et p2
    
    ->Parametres : p1 : coordonnes de p1 (liste d'entiers)  
                   p2 : coordonnes de p2 (liste d'entiers)  
                   
    -> Retour : distance separant p1 et p2 (float)
    Exemple : distance([0,1] , [1,1]) renvoie 1.0
    '''
    somme=0
    for i in range(len(p1)):
        somme+=(p1[i]-p2[i])**2
    return sqrt(somme)

def distance_voisins(p1,jeu2donnees):
    '''
    Aide de la fonction distance_voisins du module knn :
    
    distance(p1,dataset)
        Calcule la distance Euclidienne separant le point p1 et des diffrents points du jeu de donnees (dataset)
    
    ->Parametres : p1 : coordonnes de p1 (liste d'entiers)  
                   jeu2donnees : liste de tuples : [('nom du joueur','poste du joueur','taille','masse')....] 
                   
    -> Retour : liste de listes contenant l'les caractéristiques du joueur et la distance entre ce joueur et le joueur p1
    Exemple : distance_voisins([180,90] , [('joueur1','arriere','175','75'), ('joueur2,'avant','190','90')]) renvoie
    [[('joueur1','arriere','175','75'), 15.811388300841896], [('joueur2,'avant','190','90'), 10.0]]
    '''
    result = []
    i=0
    for i in range(len(jeu2donnees)):
        result.append([jeu2donnees[i],distance(p1,[int(jeu2donnees[i][2]),int(jeu2donnees[i][3])])])
    return result

def k_voisins(distances,k) :
    '''
    Aide la fonction K_voisins du module Knn :
    
    k_voisins(jeu2donnees,k)
        Renvoie la liste des K plus proches voisins à partir de la liste des distances
    Parametres : distances : liste de listes contenant les caracteristiques du joueur et la distance entre ce joueur et le joueur p1
                    K : nombre de voisins considérés (int)
    Retour : Liste des K plus proches joueurs
    '''
    k_voisins = []    
    for i in range(k) :
        dmin = distances[0][1]
        index = 0
        for i in range(len(distances)) :
            if distances[i][1] < dmin :
                dmin = distances[i][1]
                index = i
        k_voisins.append(distances.pop(index))
    return k_voisins
        
def predire_classe(k_voisins):
    '''
    Aide de la fonction predire_classe du module knn :
    
    predire_classe(proches joueurs)
        Renvoie la classe plus proche voisin du point p1 
    
    ->Parametres : k_voisins : liste des k voisins 
                   
    -> Retour : Poste (classe) du plus proche voisin de p1
    '''
    postes = {}
    #Creer dictionnaire avec classes et nombre d'occurrence de chaque classe
    for joueur in k_voisins :
        if joueur[0][1] in postes :
            postes[joueur[0][1]] +=1
        else :
            postes[joueur[0][1]] = 1
    #Cherche maximum du nombre d'occurence
    n = 0
    for classe in postes :
        if postes[classe] > n :
             n = postes[classe]
             classe_majoritaire = classe
    return classe_majoritaire
    


dataset = extractionDonnees("joueursToulouse.csv")
distances = distance_voisins([185,114],dataset)
kNN = k_voisins(distances,10)
prediction = predire_classe(kNN)