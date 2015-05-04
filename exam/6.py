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

def insert(x,ss):
	rs = []
	# def loop (ss, rs):
	while not null(ss):

		if x <= head(ss):
			# rs = snoc(rs, x)

			return contact( snoc(rs,x) , ss )
			# return snoc(rs, x)
			

		else:
			rs = snoc(rs, head(ss))
			ss = tail(ss)
			
			# return loop(tail(ss), snoc(rs, head(ss)))

	# else:
	# 	ss = tail(ss)
	# 	rs = nil
	return snoc(rs, x)


def isort(xs):
	rs = nil

	while not null(xs):
		rs = insert(head(xs), rs)
		xs = tail(xs)
		# return loop(tail(xs), insert(head(xs), rs ))
	# else:
	return rs

	# return loop(xs, nil)

def smaller(x,y):
	if x < y : return x
	else: return y


# def smallest(xs):
# 	if length(xs) > 1:
# 		x = smallest(tail(xs))
# 		return smaller(head(xs), x)
# 	else:
# 		return head(xs)

def smallest(xs):
	def loop(xs, rs):

		if length(xs) > 1:
			# rs = smallest(tail(xs))
			# print(rs)
			return loop(tail(xs), smaller(head(xs), rs))
		else:
			return rs

	return loop(xs,head(xs))


nil = []
list1 = cons(23,cons(8,cons(5,cons(40,cons(10,nil)))))
s = int(input("?"))
print(list1)
# list1 = isort(list1)
# list1 = insert(4, list1)
list1 = smallest(list1)
print(list1)