from microbit import *
import neopixel


# Setup the Neopixel strip on pin0 with a length of 8 pixels

np = None
OFF = (0, 0, 0)
couleur = (255, 255, 255)

def color(rgb):
    global couleur
    couleur = rgb


def connect(port):
    '''Creer un port de communication'''
    global np
    np = neopixel.NeoPixel(port, 30)
    np.clear()

def lightOn(mask, verbose = False):
    mask_bin = bin(mask)[2:]
    mask_bin = '0'*(30-len(mask_bin)) + mask_bin
    if verbose :
        print(mask_bin)
    for i in range(len(mask_bin)):
        if mask_bin[i] == '1':
            np[i] = couleur
        else:
            np[i] = OFF
    np.show()