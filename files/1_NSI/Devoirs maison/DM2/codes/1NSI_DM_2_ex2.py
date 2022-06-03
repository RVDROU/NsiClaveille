from turtle import *
def polygone(nb_etapes, longueur_cote):
    for i in range(nb_etapes):
        forward(longueur_cote)
        left(360/nb_etapes)

# Q3
#polygone(5,50)

# Q4
#polygone(4,100)
#polygone(100,4)


# Q5
def figure1() :
    for i in range(5) :
        polygone(7, 20)
        forward(60)
    
def figure2() :
    for i in range(5) :
        polygone(5,20)
        forward(60)
        left(360//5)
