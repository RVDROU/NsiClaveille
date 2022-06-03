x = 5
def sommeFonction(a, b) :
    print('             -> ma_variable dans la fonction avant calcul : ', x)
    z = a + b + x
    print('             -> ma_variable dans la fonction après calcul : ', x)
    return z

print('ma_variable avant fonction : ', x)
r = sommeFonction(4,6)
print('ma_variable après fonction : ', x)
