#coding: utf-8

def even(number):
	return number % 2 == 0
def odd(number):
	return number % 2 != 0

def gcd(m,n) : 
	def loop (m, n, result):

	    if m == 0 or n == 0 :  # 종료조건
	        if m == 0 :  
	            return n*result
	        else : # n == 0 
	            return m*result
	    else :               # 재귀호출조건
	        if even(m) and even(n) : 
	            return loop(m//2,n//2,result*2) 
	        elif even(m) and odd(n) : 
	            return loop(m//2,n,result) 
	        elif odd(m) and even(n) : 
	            return loop(m,n//2,result) 
	        elif m <= n : 
	            return loop(m,(n-m)//2,result) 
	        elif m >= n : 
	            return loop(n,(m-n)//2,result)

	return loop(m, n, 1)


m = input("m?")
n = input("n?")

print( gcd( int(m), int(n) ) )