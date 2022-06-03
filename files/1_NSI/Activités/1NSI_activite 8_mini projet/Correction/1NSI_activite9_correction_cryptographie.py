# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:41:07 2018

@author: herve.drougard
"""
def decrypteCle(message,cle):
    '''
    decrypte le message avec la cle
    
    Arguments :
    message : message crypte (string)
    cle : cle de cryptage (string)

    Retour
    message moins la cle et sans espace (string)
    '''
    messageDecrypt=''
    messageLst = message.split(' ')  #Decoupe le message en une liste d'elements de 5 chiffres (string)
    for bloc in messageLst : #balayage des elements de 5 chiffres du message
        # Retrancher la cle au code de 5 caracteres contenus dans bloc. Le resultat
        # des operations sont a placer en suivant dans la variable messageDecrypt (string)
            #####################################
            ##    Zone A completer par       ####
            ###    plusieurs instructions     ###
            #####################################
    
    return messageDecrypt

def decoupeTexteCrypte(message,tableAlphabet):
    """
    Decoupe chaque caractere du message crypte MOINS LA CLE 
    en fonction de la table d'alphabet
    Arguments :
    message : message moins la cle (string)
    tableAlphabet : Liste des codes alphabétiques (liste de string)

    Retour
    Listes des valeurs codees decoupees selon l’alphabet (string)
    """

    messageDecoupe=[]
    while len(message)>0:
## Test si le premier caractere du message est dans l'alphabet
        if message[0] in tableAlphabet : 
## Si oui ajoute la valeur a la table et detruit le caractere du message            
            messageDecoupe.append(message[0])
            message=message[1:]
            
        else :
## Sinon ajoute les deux premiers caracteres a la table 
            #####################################
            ## A completer par une instruction###
            #####################################

## puis detruit les deux carcatere du message
           ######################################
           ## A completer par une instruction####
           ######################################
        
##Renvoie le message decoupe dans une liste   
    return messageDecoupe
    

        
def decrypteAlphabet(messageCoupe,tableAlphabet):
    """Decrypter le message selon l'alphabet
    Arguments d'entree : 
    message : message sous forme de liste de caracteres codes (type string)
    tableAlphabet : Alphabet sous la forme d une liste de lettre codees (type string)
    retour :
    message decrypte (type string)
    """

    alphabet='abcdefghijklmnopqrstuvwxyz'
    messageDecrypte=''
#Pour chaque caractere coupe
    for caractere in messageCoupe:
        positionDansTable=tableAlphabet.index(caractere) ##recherche position du nombre dans la table alphabet
        caractereDecode=alphabet[positionDansTable] ##Convertir le nombre en lettre
        messageDecrypte=messageDecrypte+caractereDecode ##Reconstruit le message en concatenant les lettres decryptees
    return messageDecrypte









