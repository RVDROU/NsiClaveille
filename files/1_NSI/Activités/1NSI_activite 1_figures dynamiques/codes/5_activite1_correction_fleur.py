# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:09:55 2018

@author: herve
"""
#Fleur
from turtle import *
reset()
speed('fastest')
up()
down()
width(2)
bgcolor("black")
color("white")
l=5
for i in range(4):
    for j in range(10):
        circle(l)
        l=l+10
        
    l=5    
    left(90)