# -*- coding: utf-8 -*-
"""
Comptage des défibrillateurs type DAE à Bordeaux
"""
import json, requests                                               
                                                            
url = 'http://odata.bordeaux.fr/v1/databordeaux/defibrillateurs/?format=json'   
resp = requests.get(url, verify=True)                                   
dico = resp.json()
count = 0
for key in dico.keys():                                         
    donnees=dico.get(key)                                           
    for i in range(len(donnees)) :
        if donnees[i].get('typologie') == 'DAE' :
            count += 1
print(count)                                

