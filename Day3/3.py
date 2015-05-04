#coding: utf-8

def isRNN(message) : 
    s = input(message) 
    (front,mid,back) = s.partition("-") 
    while not (format_ok(front,mid,back) and last_digit_ok(front+back)) : 
        print ("Invalid number")
        s = input(message)
        (front,mid,back) = s.partition("-")
    return s

def format_ok(f,m,b) :
	if( (f.isdigit() and len(f) == 6) and (m == '-') and (b.isdigit() and len(b) == 7) ) :
		return True


def last_digit_ok(s) : 

	return int(s[12])  == 11 - (int(( 2 * int(s[0]) + 3 * int(s[1]) + 4 * int(s[2]) + 5 * int(s[3]) + 6 * int(s[4]) + 7 * int(s[5]) + 8 * int(s[6]) + 9 * int(s[7]) + 2 * int(s[8]) + 3 * int(s[9]) + 4 * int(s[10]) + 5 * int(s[11])) % 11 ))

	

result = isRNN("주")

print (result)