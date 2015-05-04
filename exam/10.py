#coding: utf-8

def gcd(m,n):
	while n != 0:
		(m, n) = n, m%n
	return m

a = int(input("A? "))
b = int(input("B? "))

print(gcd(a,b))