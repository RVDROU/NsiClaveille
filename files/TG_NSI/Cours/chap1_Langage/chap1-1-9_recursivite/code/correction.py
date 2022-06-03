#def somme(n):
#    if n==1:
#        return 1
#    else :
#        return n**2+somme(n-1)

#def calculElemPositifs(tab) :
#    if len(tab)==1 :
#        if tab[0]>0 :
#            return tab[0]
#        else :
#            return 0
#    else :
#        if tab[0]>0 :
#            return tab[0]+calculElemPositifs(tab[1:])
#        else :
#            return calculElemPositifs(tab[1:])

#def inverse(chaine):
#    if len(chaine)==1 :
#        return chaine
#    else :
#        return inverse(chaine[1:])+chaine[0]

def sommeElem(chaine):
    if len(chaine)==1 :
        return int(chaine)
    else :
        return int(chaine[0])+sommeElem(chaine[1:])
    
def sommeElem2(chaine,cumul = 0):
    if len(chaine)==1 :
        return cumul + int(chaine[0])
    else :
        return sommeElem2(chaine[1:], cumul + int(chaine[0]))
