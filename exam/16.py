#coding: utf-8
def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 

def even(number):
	return number % 2 == 0
def odd(number):
	return number % 2 != 0


def multi(m,n):
	def loop(m, n, rs):
		if n > 0:
			if even(n) :
				return loop(double(m), halve(n), rs)
				# return multi(double(m),halve(n))
			else:
				return loop(m, n - 1, rs + m)
				# return m + multi(m,n-1)
		else:
			return rs

	return loop(m,n,0)



a = int(input("A? "))
b = int(input("B? "))

print(multi(a,b))