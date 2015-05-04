#coding: utf-8

def get_int(message) : 
    s = input(message) 
    while not s.isdigit() : 
        s = input(message) 
    return int(s)

def remove_sign(text):
	if(text[0] == '+' or text[0] == '-'):
		return text[1:]
	return text

def get_int_signed(message):
	s = input(message)
	while not remove_sign(s).isdigit()  : 
		s = input(message)
	return int(s)



s = get_int_signed("정수를 입력해주세요.")

print (s)

# s = -30
# print (s)