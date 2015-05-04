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


def insert(xs, x):
	if not null(xs):
		if n < head(xs):
			return
		else:
			



nil = []
list1 = cons(23,cons(8,cons(5,cons(38,cons(12,nil)))))
s = int(input("?"))
print(list1)
# list1 = isort(list1)
# list1 = insert(4, list1)
# list1 = smallest(list1)
list1 = ssort(list1)
print(list1)
