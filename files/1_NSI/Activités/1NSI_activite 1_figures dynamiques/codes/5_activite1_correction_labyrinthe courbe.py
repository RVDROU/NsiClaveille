# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:09:55 2018

@author: herve
"""

#labyrinthe courbé
from turtle import *
reset()
speed('fastest')
up()
down()
l=5
for i in range(180):
    forward(l)
    left(90.5)
    l=l+3