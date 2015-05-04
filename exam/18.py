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
	def loop(m,n):
		if n > 1:
			if(odd(n)):
				return m + loop(double(m),halve(n))
			else:
				return loop(double(m),halve(n))
		else:
			return m

	if n > 0:
		return loop(m,n)
	else:
		return 0


a = int(input("A? "))
b = int(input("B? "))

print(multi(a,b))