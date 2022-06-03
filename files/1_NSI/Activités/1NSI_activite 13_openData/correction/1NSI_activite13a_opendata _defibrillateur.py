# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:01:37 2018

@author: herve
"""

import json, requests
from math import sqrt, inf

def calcul_distance(x_p,y_p,x_borne,y_borne):
    '''Calcul de distance entre position et borne'''
    distance=sqrt((x_borne-x_p)**2+(y_borne-y_p)**2)
    return distance

   
def bornes_proches(distance):
    '''Identification de l'ID des 6 bornes proches '''
    bornes=[]    
    for i in range(6) :
        mini = inf
        indice_distance = 0
        for j in range(len(distance)) :
            if distance[j][0] < mini and not (distance[j] in bornes) :
                mini = distance[j][0]
                indice_distance = j
        bornes.append(distance[indice_distance])
    return bornes


def afficher_list(data,distance_bornes):
    '''Affichage des adresses des 6 bornes    '''
    for i in range(len(distance_bornes)):
        indice = distance_bornes[i][1]
        print(data[indice].get("adresse")) 



url = 'http://odata.bordeaux.fr/v1/databordeaux/defibrillateurs/?format=json'
resp = requests.get(url, verify=True) 
dico = resp.json()
dist = []
x = -0.56
y = 44.86
##Balayage des défibrilateurs
for key in dico.keys():
    donnees=dico.get(key)   
    for i in range(len(donnees)):
        ##Calcul de la distance
        d = calcul_distance(x,y,float(donnees[i].get("x_long")),float(donnees[i].get("y_lat")))
        dist.append((d, i))

##Extraction des 6 bornes les plus proches
indice_bornes=bornes_proches(dist)
afficher_list(donnees,indice_bornes)
    
  
        
    