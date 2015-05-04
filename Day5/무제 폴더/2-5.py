#coding: utf-8

def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 

def mult(m,n) :
	result = 0
	i = 0
	while(n > 0):
		if( n % 2 == 0):
			m =double(m)
			n = halve(n)
		else:
			n = n - 1
			result = result + m

	return result

m = int(input("m?"))
n = int(input("n?"))
print(mult(m,n))
