#coding: utf-8

def gugudan1():
	for i in range(2,10):
		# print("1")
		for j in range(1,10):
			# print(i)
			# print(j)
			print(str(i) + " X " + str(j) + " = " + str((i)*(j)), end="  ")
			if(j%3 == 0):
				print("")
		print("")

gugudan1()