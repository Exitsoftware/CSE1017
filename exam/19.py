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
	def loop(m,n,rs):
		if n > 1:
			if(odd(n)):
				return loop(double(m),halve(n),rs+m)
			else:
				return loop(double(m),halve(n),rs)
		else:
			return rs + m

	if n > 0:
		return loop(m,n,0)
	else:
		return 0


a = int(input("A? "))
b = int(input("B? "))

print(multi(a,b))