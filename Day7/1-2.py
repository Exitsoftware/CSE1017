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

def gugudan2():
	
	for i in range(1,10):
		for j in range(2,6):
			print(str(j) + " X " + str(i) + " = " + str(i * j).rjust(2), end="    ")
			# if(j%5 == 0):
				# print("")
		print("")
	print("")

	for i in range(1,10):
		for j in range(6,10):
			# if(i * j < 10):
			# 	print(str(j) + " X " + str(i) + " =  " + str(i * j), end="    ")
			# else:
			print(str(j) + " X " + str(i) + " = " + str(i * j).rjust(2), end="    ")
			if(j%5 == 0):
				print("")
		print("")



gugudan2()