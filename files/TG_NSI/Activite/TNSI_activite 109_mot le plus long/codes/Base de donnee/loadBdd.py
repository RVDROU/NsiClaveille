""" Exemple de sélection d'items dans la base Lexique382 """
import re
import csv
import mysql.connector as sgbd      # importe la bibliothèque
import mysql.connector as sgbd      # importe la bibliothèque


# Curseur MariadB
mydb = sgbd.connect(            # se connecte à la DB myDatabase
        host="176.181.118.75",
        port = 3306,
        user="admin",
        password="droopy",

)

# Prepararion de s correspondances
id = 0
lemme={}
cgram={}
with open('Lexique383.tsv', newline='') as csvfile:
    reader = csv.DictReader(csvfile,delimiter='\t')
    for row in reader :
        if re.search("[\s'-]",row['ortho']+row['lemme']) is None :
               
            id +=1
            if row['lemme'] not in lemme : lemme[row['lemme']] = 'NULL'
            if row['ortho'] in lemme :
                lemme[row['ortho']] = id
            if row['cgram'] not in cgram : cgram[row['cgram']] = len(cgram)+1



mycursor = mydb.cursor()

# Creation des tables
requetes = ['DROP TABLE IF EXISTS DICTIONNAIRE.lexico;','DROP TABLE IF EXISTS DICTIONNAIRE.gram;',
            'CREATE TABLE DICTIONNAIRE.lexico (id INT NOT NULL, mot varchar(50) NOT NULL, lemme int,cgram int, freq float, PRIMARY KEY(id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;',
            'CREATE TABLE DICTIONNAIRE.gram (id_cg INT NOT NULL, cgram varchar(50) NOT NULL, PRIMARY KEY(id_cg)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;']

for req in requetes :
    mycursor.execute(req)



# Mise à jour de cgram

requete = 'INSERT INTO DICTIONNAIRE.gram(id_cg,cgram) VALUES '
for cle in cgram :
    requete += '('+str(cgram[cle])+",'"+ cle +"'),"

requete = requete[:-1] + ';'
mycursor.execute(requete)
mydb.commit()

# Mise à jour table lexico
id = 0
requete = 'INSERT INTO DICTIONNAIRE.lexico(id,mot, lemme,cgram, freq) VALUES '
with open('Lexique383.tsv', newline='') as csvfile:
    reader = csv.DictReader(csvfile,delimiter='\t')
    for row in reader :
        if re.search("[\s'-]",row['ortho']+row['lemme']) is None :
            id +=1
            requete += '('+str(id)+",'"+ row['ortho'] +"',"+ str(lemme[row['lemme']]) +','+ str(cgram[row['cgram']])+','+ str(row['freqlemlivres']) +"),"
            if id%200 == 0 :
                requete = requete[:-1] + ';'
                mycursor.execute(requete)
                mydb.commit()
                print(requete)
                requete = 'INSERT INTO DICTIONNAIRE.lexico(id,mot, lemme,cgram, freq) VALUES '
                





mydb.close() 
# INSERT INTO `ADHESION` (`AD_COUREUR_FK`, `AD_ANNEE`, `AD_LICENCE`, `AD_COTISATION`, `AD_CLUB_FK`) VALUES
# (1, 2015, '314156', 43, 1),

