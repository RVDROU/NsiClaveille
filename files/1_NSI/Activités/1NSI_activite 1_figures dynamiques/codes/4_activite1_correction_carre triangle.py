from turtle import*
setup(1200, 600)
up()
goto(-600,0)
down()
l=30
for i in range(8) :
    color('blue')
    for i in range(4) :
        forward(l)
        right(90)
    up()
    forward(l+20)
    color('red')
    down()
    for i in range(3) :
        forward(l)
        right(120)
    up()
    forward(l+20)
    down()
    l+=20