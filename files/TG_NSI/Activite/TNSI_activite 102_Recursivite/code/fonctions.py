def h(x):
   return x+1
def g(x):
   return h(x) + 2 + k(x+1)
def f(x):
   return g(x) + 1
def k(x):
   return x+1

def factorielle(n):
   if n==1 : return 1
   else : return n*factorielle(n-1)