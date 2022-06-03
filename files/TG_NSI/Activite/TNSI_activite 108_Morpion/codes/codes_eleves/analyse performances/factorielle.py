def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def calcul_temps(n : int) :
	return factorial(n) * 50 * 1*10**(-9)