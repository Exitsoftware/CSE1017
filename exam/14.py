#coding: utf-8
def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 

def even(number):
	return number % 2 == 0
def odd(number):
	return number % 2 != 0

# def multi(m,n):
# 	if n > 0:
# 		return m + multi(m, n-1)
# 	else:
# 		return 0


# def multi(m,n):
# 	def loop(n,rs):

# 		if n > 0 :
# 			return loop(n-1, rs + m)
# 		else:
# 			return rs


# 	return loop(n,0)


def multi(m,n):
	# def loop(n,rs):

	rs = 0

	while n > 0 :
		(n, rs) = n - 1, rs + m
		# return loop(n-1, rs + m)

	return rs


	# return loop(n,0)



a = int(input("A? "))
b = int(input("B? "))

print(multi(a,b))