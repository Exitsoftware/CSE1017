#coding: utf-8

def even(number):
	return number % 2 == 0
def odd(number):
	return number % 2 != 0

def gcd(m,n) : 
	result = 1
	while(True):
		if m == 0 or n == 0 :  # 종료조건
			if m == 0 :  
				return n * result
			else : # n == 0 
				return m * result
	    # else :               # 재귀호출조건
		if even(m) and even(n) :
			m = m//2
			n = n//2
			result = result * 2
		elif even(m) and odd(n) : 
			m = m//2
		elif odd(m) and even(n) : 
			n = n//2
		elif m <= n : 
			n = (n-m)//2
		elif m >= n :
			m, n = n, (m-n)//2

m = input("m?")
n = input("n?")

print( gcd( int(m), int(n) ) )