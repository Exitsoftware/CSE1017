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


def count(x, xs):
	result = 0
	while(not null(xs)):
		if(head(xs) == x):
			xs = tail(xs)
			result = result + 1
			# return loop(tail(xs), result + 1)
		else:
			xs = tail(xs)
			# return loop(tail(xs), result)
	# else:
	return result
	# return loop(xs, 0)

def remove_one(x, xs):
	def loop(xs, rs):
		if(not null(xs)):
			if(head(xs) == x):
				return contact(rs, tail(xs))
				# return tail(xs)
			else:
				return loop(tail(xs), snoc(rs, head(xs)))
				# return cons(head(xs), remove_one(x, tail(xs)))
		else:
			return rs
		# else:
		# 	return result
	# else:
	return loop(xs, nil)


nil = []
list1 = cons(3,cons(3,cons(5,cons(3,cons(10,nil)))))
s = int(input("?"))

print(count(s, list1))
print(remove_one(s, list1))