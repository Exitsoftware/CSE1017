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
	if n > 0:
		if even(n) :
			return multi(double(m),halve(n))
		else:
			return m + multi(m,n-1)
	else:
		return 0




a = int(input("A? "))
b = int(input("B? "))

print(multi(a,b))