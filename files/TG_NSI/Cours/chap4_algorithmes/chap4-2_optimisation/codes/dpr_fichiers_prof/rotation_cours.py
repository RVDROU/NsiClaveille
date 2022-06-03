import copy
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

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
    image = np.array(Image.open('r2d2.jpg'))
    image_complete = image
    image = rotate_construction_cours(image, etape)
    affiche_image_croix(etape)
    affiche_image_croix(etape + 1)
    plt.imshow(image)
    plt.show()
    

