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
	x = head(xs)	
	xs = tail(xs)
	

	while not null(xs):
		x = smaller(head(xs), x)
		xs = tail(xs)

	return x

# def smallest(xs) :
#     (x,xs) = (head(xs),tail(xs))
#     while not null(xs) :
#         x = smaller(head(xs),x)
#         xs = tail(xs)
#     return x

	# return loop(xs,head(xs))

# def ssort(xs) :
#     if not null(xs) :
#         x = smallest(xs)
#         return cons(x,ssort(remove_one(x,xs)))
#     else :
#         return nil

def ssort(xs) :
	def loop(xs, rs):

		if not null(xs) :
			print(xs)
			x = smallest(xs)
			print("x = " + str(x))
			return loop(remove_one(x, xs) , snoc(rs, x) )
			# return cons(x,ssort(remove_one(x,xs)))
		else :
			return rs

	return loop(xs, nil)


nil = []
list1 = cons(23,cons(8,cons(5,cons(38,cons(12,nil)))))
s = int(input("?"))
print(list1)
# list1 = isort(list1)
# list1 = insert(4, list1)
# list1 = smallest(list1)
list1 = ssort(list1)
print(list1)
