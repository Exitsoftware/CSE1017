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
		# return cons(x, nil)

	# return loop(ss, nil)

# def isort(xs):
# 	if not null(xs):
# 		return insert(head(xs), isort(tail(xs)))
# 	else:
# 		return nil

def isort(xs):
	def loop(xs, rs):
		if not null(xs):
			print("F")
			print(rs)
			return loop(tail(xs), insert(head(xs), rs ))
		else:
			return rs

	return loop(xs, nil)

nil = []
list1 = cons(23,cons(8,cons(5,cons(40,cons(10,nil)))))
s = int(input("?"))
print(list1)
list1 = isort(list1)
# list1 = insert(4, list1)

print(list1)