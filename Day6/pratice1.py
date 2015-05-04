#coding: utf-8

def cons(x, xs):
	return [x] + xs
def head(xs):
	return xs[0]
def tail(xs):
	return xs[1:]
def null(xs):
	return xs == nil
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

def exist(x, xs):

	while(not null(xs)):
		if(head(xs) == x):
			return True
		else:
			xs = tail(xs)

	return False


def count(x, xs):
	result = 0
	while(not null(xs)):
		if(head(xs) == x):
			xs = tail(xs)
			result = result + 1
		else:
			xs = tail(xs)
	return result

def remove_one(x, xs):
	def loop(xs, rs):
		if(not null(xs)):
			if(head(xs) == x):
				return contact(rs, tail(xs))
			else:
				return loop(tail(xs), snoc(rs, head(xs)))
		else:
			return rs
	return loop(xs, nil)

def isort(xs):
	if(not null(xs)):
		return insert(head(xs), isort(tail(xs)))
	else:
		return nil

def insert(x, xs):
	if(not null(xs)):
		if( x <= head(xs)):
			# print("F")
			return cons(x, xs)
			# return cons(head(xs), insert(x, tail(xs)))
		else:
			# print("@")
			return cons(head(xs), insert(x, tail(xs)))
			# print("f")
			# return insert(x, xs)
	else:
		# print("#")
		return cons(x, nil)
	# if(xs == nil):
	# 	return cons(x, nil)
	# elif(x > head(xs)):
	# 	return cons(head(xs), insert(x, tail(xs)))
	# else:
	# 	return insert(x, xs)


nil = []
list1 = cons(3,cons(7,cons(5,cons(40,cons(10,nil)))))
s = int(input("?"))
# print("#")
# print(count(s, list1))
# print(remove_one(s, list1))
list1 = isort(list1)
print(list1)
