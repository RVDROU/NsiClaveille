# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:07:16 2018

@author: herve
"""

#Rosace
from turtle import *
reset()
speed("fastest")
color("black")
for i in range(36):
    if i%3==0:
        color('red')
    elif i%3==1:
        color('orange')
    else :
        color('yellow')
    circle(80)
    left(10)
