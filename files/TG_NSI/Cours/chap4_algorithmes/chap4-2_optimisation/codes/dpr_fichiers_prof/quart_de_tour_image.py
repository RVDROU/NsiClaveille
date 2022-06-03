# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:59:56 2020

"""


import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


"""
Rotation d'un quart de tour d'image de taille 2**p x 2**p
Diviser pour régner : coût en mémoire proportionnel à la taille de image 
"""

def rotate(image):
    n = len(image)
    if n > 1:
        temp = np.copy(image[n//2:, :n//2])
        image[n//2:, :n//2] = rotate(image[n//2:, n//2:])
        image[n//2:, n//2:] = rotate(image[:n//2, n//2:])
        image[:n//2, n//2:] = rotate(image[:n//2, :n//2])
        image[:n//2, :n//2] = rotate(temp)
    return image

image = np.array(Image.open('R2D2.jpg'))
image = rotate(image)
plt.imshow(image)



"""
Rotation d'un quart de tour d'image de taille 2**p x 2**p
en appliquant une permutation circulaire sur les quatre blocs
point par point pour éviter de stocker un quart de l'image en mémoire.
Je ne comprends pas l'intérêt... 
Autant effectuer la rotation directement ...
"""

def rotate(image):
    n = len(image)
    if n > 1:
        n = len(image)
        for i in range(n//2):
            for j in range(n//2):
                temp = np.copy(image[i, j])
                image[i, j] = image[i + n//2, j]
                image[i + n//2, j] = image[i + n//2, j + n//2] 
                image[i + n//2, j + n//2] = image[i, j + n//2] 
                image[i, j + n//2] = temp
        # Rotation de chaque bloc
        rotate(image[:n//2, :n//2])
        rotate(image[:n//2, n//2:])
        rotate(image[n//2:, :n//2])
        rotate(image[n//2:, n//2:])
    return image

image = np.array(Image.open('r2d2.jpg'))
image = rotate(image)
plt.imshow(image)




"""
Version classique (itérative)
Rotation d'un quart de tour d'image de taille n x n
Permutation : image[i, j] -> image[j, n - i] -> image[n - i, n - j] -> image[n - j, i]
"""

def rotate(image):
    n = len(image)
    for i in range(n//2):
        for j in range(n//2):
            temp = np.copy(image[n - 1 - j, i])
            image[n - 1 - j, i] = image[n - 1 - i, n - 1 - j]
            image[n - 1 - i, n - 1 - j] = image[j, n - 1 - i]
            image[j, n - 1 - i] = image[i, j]
            image[i, j] = temp
    return image

image = np.array(Image.open('vador.jpg'))
image = rotate(image)
plt.imshow(image)



"""
Version itérative
Rotation d'un quart de tour d'image de taille m x n
Impossible avec cout en mémoire constant car obligation de créer 
un autre tableau puisque dimensions différentes
"""

def rotate(image):
    dim = list(image.shape)
    dim[0], dim[1] = dim[1], dim[0]
    nimage = np.empty(dim, np.uint8)
    n, m = nimage.shape[0:2]
    for i in range(n):
        for j in range(m):
            nimage[i, j] = image[m - 1 - j, i]
    return nimage

image = np.array(Image.open('yoda.jpg'))
image = rotate(image)
plt.imshow(image)


"""
Utilisation de ndimage.rotate
"""

from scipy import ndimage

image = np.array(Image.open('yoda.jpg'))
image = ndimage.rotate(image, -90)
plt.imshow(image)



"""
Version pour construire les graphiques servant à illustrer le cours
"""

import copy

def affiche_image_croix(d):
    def dessin_croix(nimage, d):
        if d >= 1:
            n = len(nimage)
            for i in range(n):
                nimage[n//2, i] = [0]*3
                nimage[i, n//2] = [0]*3
            dessin_croix(nimage[n//2:, :n//2], d-1)
            dessin_croix(nimage[n//2:, n//2:], d-1)
            dessin_croix(nimage[:n//2, n//2:], d-1)
            dessin_croix(nimage[:n//2, :n//2], d-1)         
              
    nimage = copy.deepcopy(image_complete)
    dessin_croix(nimage, d)
    plt.imshow(nimage)
    plt.show()
    

def rotate_construction_cours(image, etape):
    n = len(image)
    if etape > 0:
        temp = np.copy(image[n//2:, :n//2])
        image[n//2:, :n//2] = image[n//2:, n//2:]
        image[n//2:, n//2:] = image[:n//2, n//2:]
        image[:n//2, n//2:] = image[:n//2, :n//2]
        image[:n//2, :n//2] = temp
        rotate_construction_cours(image[n//2:, :n//2], etape - 1)
        rotate_construction_cours(image[n//2:, n//2:], etape - 1)
        rotate_construction_cours(image[:n//2, n//2:], etape - 1)
        rotate_construction_cours(image[:n//2, :n//2], etape - 1)
    return image

for etape in range(9):
    image = np.array(Image.open('R2D2.jpg'))
    image_complete = image
    image = rotate_construction_cours(image, etape)
    affiche_image_croix(etape)
    affiche_image_croix(etape + 1)
    plt.imshow(image)
    plt.show()
    




