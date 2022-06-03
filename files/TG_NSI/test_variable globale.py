x = 0
def fonction() :
    a = x + 1
    print('          ->  ma_variable dans fonction : ', a)
    x = 1
    print('          ->  ma_variable dans fonction après modification : ', x)
    
print('ma_variable avant fonction : ', x)
fonction()
print('ma_variable après fonction : ', x)