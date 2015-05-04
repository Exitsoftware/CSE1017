def gcd(m,n) : 
	while(n > 0):
		temp = m % n
		m = n
		n = temp

	return m

def even(number):
	return number % 2 == 0
def odd(number):
	return number % 2 != 0



s = int(input("?"))
m = int(input("?"))
print(gcd(s, m))c