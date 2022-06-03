from turtle import *
#1 carre
reset()

#carré rouge
speed('fastest')
color('red')
for i in range(10):
    for i in range(4) :
        forward(20)
        left(90)
    up()
    forward(30)
    down()
done()