def mult(a, b) :
    return a * b

def fact(n) :
''' factorielle
'''
    f = 1
    for i in range(2,n+1) :
        f = mult(f,i)
    return f

fact(4)

    