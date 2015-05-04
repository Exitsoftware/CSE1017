#coding: utf-8

def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 

def mult(m, n) :
	result = 0

	if (n == 1):
		return m
	elif (n == 0):
		return 0

	while(True):
		if (n == 1):
			result = result + m
		if(n % 2 == 0):
			m = double(m)
			n = halve(n)
		else:
			m = double(m)
			n = halve(n)
			result = result + m

	return mult(m, n)

m = int(input("m?"))
n = int(input("n?"))
print(mult(m,n))