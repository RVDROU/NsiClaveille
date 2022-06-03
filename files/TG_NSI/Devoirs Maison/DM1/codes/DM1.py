import math
from haversine import haversine
# class CodeCesar:
#     def __init__(self, cle):
#         self.cle = cle
#         self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     
#     def decale(self, lettre):
#         num1 = self.alphabet.find(lettre)
#         num2 = num1+self.cle
#         if num2 >= 26:
#             num2 = num2-26
#         if num2 < 0:
#             num2 = num2+26
#         nouvelle_lettre = self.alphabet[num2]
#         return nouvelle_lettre
#     
#     def cryptage(self, texte) :
#         crypte =''
#         for l in texte :
#             crypte = crypte + self.decale(l)
#         return crypte
# 
#     def transforme(self, texte):
#         self.cle = -self.cle
#         message = self.cryptage(texte)
#         self.cle = -self.cle
#         return message
# 
# print(CodeCesar(10).transforme("PSX"))
# 
# # n = int(input('Saisir la cle de cryptage'))
# # code = CodeCesar(n)
# # texte = input('Saisir texte à crypter')
# # print(code.cryptage(texte))


#### Exercice 2 ####
flotte = {
12 : {"type" : "electrique", "etat" : 1, "station" : "Prefecture"},
80 : {"type" : "classique", "etat" : 0, "station" : "Saint-Leu"},
45 : {"type" : "classique", "etat" : 1, "station" : "Baraban"},
41 : {"type" : "classique", "etat" : -1, "station" : "Citadelle"},
26 : {"type" : "classique", "etat" : 1, "station" : "Coliseum"},
28 : {"type" : "electrique", "etat" : 0, "station" : "Coliseum"},
74 : {"type" : "electrique", "etat" : 1, "station" : "Jacobins"},
13 : {"type" : "classique", "etat" : 0, "station" : "Citadelle"},
83 : {"type" : "classique", "etat" : -1, "station" : "Saint-Leu"},
22 : {"type" : "electrique", "etat" : -1, "station" : "Joffre"}
}
stations = {                                    
'Prefecture' : (49.8905, 2.2967) ,                  
'Saint-Leu' : (49.8982, 2.3017),                        
'Coliseum' : (49.8942, 2.2874),                     
'Jacobins' : (49.8912, 2.3016)                      
}   

def velo_proche(pos) :
    liste_stations = []
    for nom in stations :
        d = distance(stations[nom], pos)
        if d < 800 :
            velos_dispo = [id_ for id_ in flotte if flotte[id_]['etat']==1 and flotte[id_]['station']==nom]
            liste_stations.append((nom, d, velos_dispo))
    return liste_stations

def distance(p1, p2) :
    return int(haversine(p1, p2) * 1000)

