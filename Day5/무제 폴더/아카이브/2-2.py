#coding: utf-8

def mult(m,n) : 
	result = 0
	while(n > 0):
		result = result + m
		n = n -1

	return result

m = int(input("m?"))
n = int(input("n?"))
print(mult(m,n))