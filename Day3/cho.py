#coding: utf-8
def get_email(message) :
    s = input(message)
    while not s.find("(") == -1 :
        s = remove_comment(s)
    s = s.partition("@")
    # print (s)
    while not (check_user_name(s[0]) and s[1] =="@" and check_domain(s[2])) :
        s= input(message)
        s.partition("@")a
    return s
     
 
def remove_comment(s) :
    a = s.find("(")
    b = s.find(")")
    s2 = s[:a] + s[b+1:]
    return s2
 
def check_user_name(s) :
    if s[0] == "." or s[len(s)-1]== "." :
        return False
    elif ".." in s :
        return False
    else :
        for i in range(0, len(s)):
            if s[i].isdigit() or s[i].isalpha() or s[i]== "!" or s[i]=="#" or s[i]=="$" or s[i]=="%" or s[i]=="&" or s[i]=="'" or s[i]=="*" or s[i]=="+" or s[i]=="-" or s[i]=="/" or s[i]=="=" or s[i]=="?" or s[i]=="^" or s[i]=="_" or s[i]=="{" or s[i]=="|" or s[i]=="}" or s[i]=="." :
                return True
            else :
                return False
                 
                 
def check_domain(s) :
    if ".." in s :
        return False
    elif (s[0] == "[" or s[len(s)-1] == "]") and (s[1:].isidgit() or ) :
        return True
    else :
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit() or s[i] == "-" or s[i] ==".":
                return True
            else :
                return False
 
 
 


print (get_email("이메일을 입력해주세요."))