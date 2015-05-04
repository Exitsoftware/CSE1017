#coding: utf-8

def double(n) : 
	return n * 2 
def halve(n) : 
	return n // 2 


def mult(m,n) :
	# def loop(m, n, result):
	if( n <= 0):
		return 0
	else:
		if( n % 2 == 0):
			# return loop(double(m), halve(n), result)
			return mult(double(m),halve(n))
		else:
			# return loop(m, n -1, result + m)
			return m + mult(m, n -1)

	return mult(m, n)

m = int(input("m?"))
n = int(input("n?"))
print(mult(m,n))
