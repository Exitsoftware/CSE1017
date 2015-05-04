#coding: utf-8

def remove_comments(s) : 
    
    start_index = s.find("(")
    end_index = s.find(")")
    
    if(str(start_index).isdigit() and str(end_index).isdigit()):
    	return (s[: start_index] + s[end_index + 1:])
    else:
    	return s

    

s = input("이메일입력")
s = remove_comments(s)

print(s)