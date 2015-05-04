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

# def ssort(x, xs):

def smallar(x,y):
	if (x < y):
		return x
	else:
		return y
# i = 0
def smallest(xs):
	
	def loop(xs, x):
		if(not null(xs)):
			# x = smallest(tail(xs))
			print(x)
			return loop( tail(xs), smallar(head(xs), x ))
			# return smallar(head(xs), x)
		else:
			return x
			# return head(xs)

	return loop(tail(xs), head(xs))

# def smallest(xs):
# 	if(length(xs) > 1):
# 		x = smallest(tail(xs))
# 		return smallar(head(xs), x)
# 	else:
# 		return head(xs)





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
	rs = nil
	# def loop(xs, rs):
	while(not null(xs)):
		# if(not null(xs)):
			# print("w")
		rs = insert(head(xs), rs)
		xs = tail(xs)

		# return loop(tail(xs), insert(head(xs), rs))
		# return insert(head(xs), isort(tail(xs)))
	# else:
	return rs
	# return loop(xs, nil)


def insert(x, xs):
	rs = nil
	while(not null(xs)):
		if( x <= head(xs)):
			return contact(rs, cons(x,xs))
		else:
			rs = snoc(rs, head(xs))
			xs = tail(xs)
			# rs = snoc(rs, head(xs))
			# return loop(tail(xs) ,snoc(rs, head(xs)))

	return snoc(rs,x)

	# return loop(xs, nil)



nil = []
list1 = cons(7,cons(3,cons(5,cons(40,cons(10,nil)))))
s = int(input("?"))
# i = 0
print(list1)
# list1 = isort(list1)
list1 = smallest(list1)
print(list1)
