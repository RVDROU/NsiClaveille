################## Exercice 1 #################

def occurence_lettres(mot):
    occur = {}
    for i in mot:
        if i in occur:
            occur[i]+=1
        else:
            occur[i] = 1
    return occur

################## Exercice 2 #################

class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse
        
    def liste_octet(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]
    
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        return self.adresse == '192.168.0.0' or self.adresse == '192.168.0.255'
    
    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l’adresse self
        si elle existe et False sinon"""
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')


''' Jeu de test de l'exercice 2 '''
assert not(AdresseIP('192.168.0.1').est_reservee()) , 'test 1 non valide'
assert AdresseIP('192.168.0.0').est_reservee() , 'test 2 non valide'
assert AdresseIP('192.168.0.2').adresse_suivante().adresse == '192.168.0.3' , 'test 3 non valide'


''' Jeu de test de l'exercice 1 '''
assert occurence_lettres('bonjour')['o'] == 2 , 'test 1 non valide'
assert occurence_lettres('Bébé')['b'] == 1 , 'test 2 non valide'
assert occurence_lettres('Bébé')['B'] == 1 , 'test 3 non valide'
assert occurence_lettres('Hello world !')[' '] == 2 , 'test 4 non valide'

