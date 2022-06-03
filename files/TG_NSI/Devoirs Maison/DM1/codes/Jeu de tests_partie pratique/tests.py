''' Jeu de tests du DM1 - classe TNSI -
Fait le 19/11/21
'''


''' Jeu de test de l'exercice 2 '''
assert not(AdresseIP('192.168.0.1').est_reservee()) , 'test 1 non valide'
assert AdresseIP('192.168.0.0').est_reservee() , 'test 2 non valide'
assert AdresseIP('192.168.0.2').adresse_suivante().adresse == '192.168.0.3' , 'test 3 non valide'


''' Jeu de test de l'exercice 1 '''
assert occurence_lettres('bonjour')['o'] == 2 , 'test 1 non valide'
assert occurence_lettres('Bébé')['b'] == 1 , 'test 2 non valide'
assert occurence_lettres('Bébé')['B'] == 1 , 'test 3 non valide'
assert occurence_lettres('Hello world !')[' '] == 2 , 'test 4 non valide'

