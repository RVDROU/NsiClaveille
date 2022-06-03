from neodriver import *
connect(pin0)

def led_gauche(nb) :
    '''fait clignoter la led 29 nb fois
    parametre nb (entier) : nombre de clignotements
    '''
    for i in range(nb) :
        lightOn(536870912, True)
        sleep(500)
        lightOn(0, True)
        sleep(500)



def double_clignotement(nb) :
    '''Commande nb clignotements alternatif des leds
    29 et 24.
    parametre nb (entier) : nombre de clignotements

    Masque -> 2**29 = 536870912  (led 29 allumee)
              2**24 = 16777216  (led 24 allumee)
    '''
    for i in range(nb) :
        lightOn(536870912, True)
        sleep(500)
        lightOn(16777216, True)
        sleep(500)


def scenario1() :
    '''Allume les leds paires puis les impaires'''
    lightOn(masque_parite(0,30))
    sleep(500)
    lightOn(masque_parite(1, 30))
    sleep(500)

def scenario1b() :
    '''Allume les leds paires puis les impaires'''
    lightOn(masque_paire(30))
    sleep(500)
    lightOn(masque_impaire(30))
    sleep(500)

def masque_paire(nb_bits) :
    '''
    Calcul le masque des bits pairs d'un nombre sur nb_bits (entier)
    '''
    masque = 0
    for i in range(nb_bits) :
        if i%2 == 0 :
            masque = masque + 2**i
    return masque


def masque_impaire(nb_bits) :
    '''
    Calcul le masque des bits pairs d'un nombre sur nb_bits (entier)
    '''
    masque = 0
    for i in range(nb_bits) :
        if i%2 == 1 :
            masque = masque + 2**i
    return masque

def masque_parite(parite, nb) :
    '''Calcul le masque selon la parité choisie.
    parametres : parite (entier) -> 0 : masque des leds paires
                                    1 : masque des leds impaires
                 nb : nombre de bits
    '''
    masque = 0
    if parite == 0 :
        debut = 0
    elif parite == 1 :
        debut = 1
    else :
        return None

    for i in range(debut, 30, 2) :
        masque = masque + 2**i
    return masque

def scenario2() :
    '''Allume les leds avec un chenillard droite -> gauche'''
    masque = 1
    for i in range(30) :
        lightOn(masque)
        sleep(100)
        masque = masque * 2

def scenario2b() :
    '''
    SOLUTION N°2
    Allume les leds avec un chenillard droite -> gauche
    '''
    masque = 1
    for i in range(30) :
        lightOn(masque)
        sleep(100)
        masque = masque << 1

def chenillard_gauche() :
    '''
    Allume les leds avec un chenillard droite -> gauche
    '''
    masque = 1
    for i in range(30) :
        lightOn(masque)
        sleep(100)
        masque = masque << 1

def chenillard_droite() :
    '''
    Allume les leds avec un chenillard droite -> gauche
    '''
    masque = 2**29
    for i in range(30) :
        lightOn(masque)
        sleep(100)
        masque = masque >> 1

def chenillard(n, type) :
    '''n allumage de chenillard selon son type
    parametres : n -> nombre d'allumage (entier)
                type (entier) -> 0 : chenillard aller
                                 1 : chenillard retour
                                 2 : chenillard aller/retour
    '''
    for i in range(n) :
        if type == 0 :
            chenillard_gauche()
        elif type == 1 :
            chenillard_droite()
        elif type == 2 :
            chenillard_gauche()
            chenillard_droite()
        else :
            return False
    return True