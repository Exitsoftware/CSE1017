#coding: utf-8

def isfloat(s) : 
    part = s.partition(".") 
    return (part[0].isdigit() and (part[2].isdigit() or part[2] == "")) or part[0] == "" and part[2].isdigit()

# def get_fixed(message) : 
#     s = input(message) 
#     while not (s.isdigit() and isfloat(s)) : 
#         s = input(message) 
#     return float(s)

def remove_sign(text):
	if(text[0] == '+' or text[0] == '-'):
		return text[1:]
	return text

# def get_int_signed(message):
# 	s = input(message)
# 	s = remove_sign(s)
# 	return int(s)


def get_fixed_signed(message) : 
    s = input(message)
    part = s.partition('.')

    while not ( isfloat(remove_sign(s))) : 
        s = input(message) 
    return float(s)

    # while not ( (remove_sign(part[0]).isdigit() and part[2].isdigit())  or isfloat(s)) : 
    #     s = input(message) 
    # return float(s)


s = get_fixed_signed("실수를 입력하세요.")

print (s)
