#coding: utf-8
import time

# def fib(n):
# 	if n > 1:
# 		return fib(n-1) + fib(n-2)
# 	else:
# 		return n

# def fib(n):
# 	def loop(k, old, new):
# 		if k < n:
# 			return loop(k+1, new, old + new)
# 		else:
# 			return new + old
# 	return loop(1,1,0)

def fib(n):
	k = 1
	old = 1
	new = 0
	while k < n:
		k , old, new = k+1, new, old+new

	return new + old

def fibs(n):
	fibs = [0,1]
	for k in range(2,n+1):
		fib = fibs[k-1]+fibs[k-2]
		fibs.append(fib)
	return fibs

n = int(input("입력하세요"))
# s = str(fib(n))

# for i in s:
# 	time.sleep(0.01)
# 	print(i)

print(fibs(n))
	