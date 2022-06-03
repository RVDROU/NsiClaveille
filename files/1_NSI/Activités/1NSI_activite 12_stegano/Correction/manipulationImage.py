# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:00:26 2019

@author: herve
"""
from PIL import Image
import numpy as np

def ouvrirImage(nomImage):
    imgPIL=Image.open(nomImage)
    img_np=np.asarray(imgPIL)
    if len(img_np.shape)==2:
        img=[[i for i in j] for j in img_np]
    elif len(img_np.shape)==3 :
        img=[[list(i[:3]) for i in j] for j in img_np]
    return img

def afficherImage(image):
    image=convertirPIL(image)
    image.show()


def convertirPIL(image):
    image_np=np.asarray(image,dtype='uint8')
    return Image.fromarray(image_np)

def sauveImage(image,nom):
    imgPIL=convertirPIL(image)
    imgPIL.save(nom)

