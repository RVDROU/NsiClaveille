# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:07:16 2018

@author: herve
"""

#ligne de carrés
from turtle import *
reset()
down()
speed("fastest")
color("black")
for j in range (10):
    for i in range(4):
      forward(20)
      left(90)
    up()
    forward(30)
    down()