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
	def loop (ss, rs):
		if not null(ss):

			if x <= head(ss):
				# rs = snoc(rs, x)
				return contact( snoc(rs,x) , ss)
				return snoc(rs, x)
				

			else:
				return loop(tail(ss), snoc(rs, head(ss)))

		else:
			return snoc(rs, x)
			# return loop(tail(ss), nil)
			# return cons(x, nil)

	return loop(ss, nil)

nil = []
list1 = cons(1,cons(3,cons(5,cons(40,cons(10,nil)))))
s = int(input("?"))
print(list1)
# list1 = isort(list1)
list1 = insert(4, list1)
print(list1)