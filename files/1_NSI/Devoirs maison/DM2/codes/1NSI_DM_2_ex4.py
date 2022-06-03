def mystere1(tab) :
    n = len(tab)
    s =''
    for i in range(n) :
        if tab[i] > i :
            s = s +'+'+str(tab[i])
    return s

def mystere2(tab) :
    i = 0
    s = 0
    c = 0
    while tab[i] < 4 :
        s = s+tab[i]
        c = c + s
        i = i + 1
    return (s,c)