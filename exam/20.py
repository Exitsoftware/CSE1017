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
	rs = 0
	# def loop(m,n,rs):
	while n > 1:
		if(odd(n)):
			(m, n, rs) = (double(m),halve(n),rs+m)
		else:
			(m, n, rs) = (double(m),halve(n),rs)

	if n > 0:
		return rs + m
	else:
		return 0


a = int(input("A? "))
b = int(input("B? "))

print(multi(a,b))