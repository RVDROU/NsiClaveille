from random import randint
a=randint(1,3)
c=21
print('il y a ',c,' allumettes')
while c!=0:
    if c==0:
        print('vous avez gagné')
        break
    elif c==1:
        print('vous avez perdu')
        break
    else:
        b=int(input("combien en prenez vous ?:"))
    if b<1:
        print('vous avez essayer de tricher donc vous avez perdu')
        break
    elif b>3:
        print('vous avez essayer de tricher donc vous avez perdu')
        break
    else:
        c=c-b
    if c==0:
        print('vous avez perdu')
        break
    elif c==1:
        print('vous avez gagné')
        break
    else:
        print('il y a ',c,' allumettes')
        z=4-b
        print('je prends',z,'allumettes')
        c=c-z
        print('il y a ',c,' allumettes')
print('on recommence ?')




