# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:09:55 2018

@author: herve
"""
#Fleur courbee
from turtle import *
reset()
speed('fastest')
up()
down()
width(2)
bgcolor("black")
couleur=["yellow","blue","green","red"]
l=5
for i in range(4):
    for j in range(10):
        color(couleur[i])
        circle(l)
        l=l+10
        left(6)
        
    l=5    
    left(30)