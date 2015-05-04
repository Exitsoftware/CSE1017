#coding: utf-8
def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 

def even(number):
	return number % 2 == 0
def odd(number):
	return number % 2 != 0


# def gcd(m,n) : 
#     if not (m == 0 or n = 0) : # 반복조건
#         if even(m) and even(n) : 
#             return 2 * gcd(m//2,n//2) 
#         elif even(m) and odd(n) : 
#             return gcd(m//2,n) 
#         elif odd(m) and even(n) : 
#             return gcd(m,n//2) 
#         elif m <= n : 
#             return gcd(m,(n m)//2) 
#         else : 
#             return gcd(n,(m n)//2) 
#     else : # 종료조건
#         if m == 0 :  
#             return n 
#         else : # n == 0 
#             return m

def gcd(m,n):
	def loop(m,n,rs):

		if not (m == 0 or n == 0):
			if even(m) and even(n):
				return loop(halve(m),halve(n), 2*rs)
			elif even(m) and odd(n):
				return loop(halve(m), n, rs)
			elif odd(m) and even(n):
				return loop(m,halve(n), rs)
			elif m <= n:
				return loop(m, halve(n-m), rs)
			else:
				return loop(n, halve(m-n), rs)
		else:
			if m == 0:
				return n * rs
			else:
				return m * rs

	return loop(m,n,1)


a = int(input("A? "))
b = int(input("B? "))

print(gcd(a,b))