#coding: utf-8

def sum(input_value):
	if(input_value < 0):
		return 0
	else:
		return input_value + sum(input_value - 1)

s = input("합?")
print(sum(int(s)))

