import csv
from math import *

def extractionDonnees(nomFichier):
    '''Aide de la fonction distance du module knn :
    
    extractionDonnees(nomfichier)
        Extrait le jeu de donnees du fichier CSV et le met en forme
    
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
    

def distance_voisins(p1,jeu2donnees):
    '''
    Aide de la fonction distance_voisins du module knn :
    
    distance(p1,dataset)
        Calcule la distance Euclidienne separant le point p1 et des diffrents points du jeu de donnees (dataset)
    
    ->Parametres : p1 : coordonnes de p1 (liste d'entiers)  
                   jeu2donnees : liste de tuples : [('nom du joueur','poste du joueur','taille','masse')....] 
                   
    -> Retour : liste de listes contenant l'indice du joueur dans le jeu de donnees et la distance entre ce joueur et le joueur p1
    Exemple : distance_voisins([180,90] , [('joueur1','arriere','175','75'), ('joueur2','avant','190','90')]) renvoie [[0, 15.811388300841896], [1, 10.0]]
    '''
   
        
def predire_classe(distances,jeu2donnees):
    '''
    Aide de la fonction predire_classe du module knn :
    
    predire_classe(distances,dataset)
        Renvoie la classe plus proche voisin du point p1 
    
    ->Parametres : distances : liste de listes contenant l'indice du joueur dans le jeu de donnees et la distance entre ce joueur et le joueur p1
                   jeu2donnees : liste de tuples : [('nom du joueur','poste du joueur','taille','masse')....] 
                   
    -> Retour : Poste (classe) du plus proche voisin de p1
    Exemple : predire_classe([[0, 15.811388300841896], [1, 10.0]] , [('joueur1','arriere','175','75'), ('joueur2,'avant','190','90')]) renvoie 'avant'
    '''



