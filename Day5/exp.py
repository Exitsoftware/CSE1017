#coding: utf-8

def exp(bottom, top):
	def loop(bottom, top, result):

		if (top == 0):
			return result
		else:
			return loop(bottom, top - 1, result * bottom)

	return loop(bottom, top, 1)


bottom = int(input("밑"))
top = int(input("위"))

print(exp(bottom, top))