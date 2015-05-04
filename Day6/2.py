#coding: utf-8

def cons(x, xs):
	return [x] + xs
def head(xs):
	return xs[0]
def tail(xs):
	return xs[1:]
def null(xs):
	# print(tail(xs))
	return tail(xs) == nil
	# return tail(xs) == None
def contact(xs, ys):
	return xs + ys
def snoc(xs, x):
	return xs + [x]

def length(xs):
	result = 0
	while(True):
		if(not null(xs)):
			xs = tail(xs)
			result = result + 1
		else:
			return result
	# return loop(xs, 0)s

def exist(x, xs):

	while(not null(xs)):
		if(head(xs) == x):
			return True
		else:
			xs = tail(xs)

	return False




nil = []
# nil = cons(3,cons(5,cons(7,cons(10,nil))))
s = int(input("?"))
list1 = cons(3,cons(5,cons(7,cons(10,nil))))
list_length = length(cons(3,cons(5,cons(7,cons(10,nil)))))
print(list_length)
print(nil)
print("\n")
print(cons(3,cons(5,cons(7,cons(10,nil)))))
print(exist(s, list1))
