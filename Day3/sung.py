#coding: utf-8

#입력
def format_ok(f,m,b) :
    if (f.isdigit()and len(f)==6 and m=="-" and b.isdigit()and len(b)==7):
        return True
    else:
        return False

def last_digit_ok(s) :
    if int(s[12]) == ( 11 - ( ( int(s[0]) * 2 + int(s[1]) * 3 + int(s[2]) * 4 + int(s[3]) * 5 + int(s[4]) * 6 + int(s[5]) * 7 + int(s[6]) * 8 + int(s[7]) * 9 + int(s[8]) * 2 + int(s[9]) * 3 + int(s[10]) * 4 + int(s[11]) * 5 ) % 11 ) ):
        return True
    else :
        return False

def isRNN(message) :
    s = input (message)
    (front,mid,back) = s.partition("-")
    while not (format_ok(front,mid,back) and last_digit_ok(front+back)) :
        print ("Invalid number")
        s = input(message)
        (front,mid,back) = s.partition("-")
    return s
#출력
#print(isRNN("input"))
print(format_ok("951013","-","1079718"))
print(last_digit_ok("9510131079718"))

