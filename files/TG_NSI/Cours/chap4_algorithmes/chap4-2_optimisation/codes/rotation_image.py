# -*- coding: utf-8 -*-
"""
Rotation image 1/4 de tour
Lycee Claveille

"""


from PIL import Image
import numpy as np
from matplotlib.pyplot import imread, imshow, show

image = imread('r2d2.jpg').tolist()
# imshow(image, cmap=('gray'))
# show()


def echangePixel(image, x1,y1,x2,y2) :
    '''echange les pixels de coodronnées (x1,y1) et (x2,y2) de image'''
    image[y1][x1],image[y2][x2] = image[y2][x2],image[y1][x1]


def echangeCarre(image,x1,y1,x2,y2,n) :
    '''echange les carres de taille n dont les coodronnées des coins sont
    (x1,y1) et (x2,y2) de image'''

    for col in range(n) :
        for ligne in range(n) :
            echangePixel(image, x1+ligne, y1+col, x2+ligne, y2+col)


def tourneCarre(image,x,y,n) :
    '''tourne l'image d'un quart de tour'''
    if n>1 :
        echangeCarre(image,x,y,x+n//2,y,n//2)
        tourneCarre(image,x+n//2,y,n//2)
        echangeCarre(image,x,y,x,y+n//2,n//2)
        tourneCarre(image,x,y,n//2)
        echangeCarre(image,x,y+n//2,x+n//2,y+n//2,n//2)
        tourneCarre(image,x,y+n//2,n//2)
        tourneCarre(image,x+n//2,y+n//2,n//2)
    

tourneCarre(image,0,0,256)
imshow(image, cmap=('gray'))
show()