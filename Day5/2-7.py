#coding: utf-8

def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 

def mult(m, n) :
	def loop(m, n, result):
		if (n == 1):
			return result + m
		if(n % 2 == 0):
			return loop(double(m), halve(n), result)
		else:
			return loop(double(m), halve(n), result + m)

	if (n == 1):
		return m
	elif (n == 0):
		return 0

	return loop(m, n, 0)

m = int(input("m?"))
n = int(input("n?"))
print(mult(m,n))