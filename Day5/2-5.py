#coding: utf-8

def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 

def mult(m, n) :
	def loop(m, n):
		if( n == 1):
			return m
		else:
			if(n % 2 == 0):
				return loop(double(m), halve(n))
			else:
				return m + loop(double(m), halve(n))

	if(n == 0):
		return 0
	else:
		return loop(m, n)

m = int(input("m?"))
n = int(input("n?"))
print(mult(m,n))