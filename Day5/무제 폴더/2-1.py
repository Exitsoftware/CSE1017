#coding: utf-8

def mult(m,n) : 
	def loop (n, result):
		if n <= 0 : 
			return result
		else : 
			return loop(n-1, result + m)

	return loop(n, 0)


m = int(input("m?"))
n = int(input("n?"))
print(mult(m,n))
