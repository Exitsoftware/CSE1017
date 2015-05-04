#coding: utf-8

# def special_str_check(s):
# 	 list = ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~" ]
# 	 count = 0

# 	 for i in list:
# 	 	if not s.find(i) == -1:
# 	 		count = count + 1
	
# 	 if count > 0:
# 	 	return True
# 	 else:
# 	 	return False

def special_str_check(s):
	 list = ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~" ]
	 # count = 0

	 for i in list:
	 	if s == i:
	 		return True
	
	 return False


def local_name_check(s):
	
	i = 0
	count = 0
	# switch = False

	while(i < len(s)):

		if ( s[i].isdigit() or s[i].isalpha() or special_str_check(s[i]) or s[i] == '.' ):
			# print(i)
			count = count + 1
			i = i + 1
		else :
			i = i + 1
		
	if (count == len(s) and dot_check(s)) :
		return True
	else :
		return False

def domain_check(s):

	i = 0
	count = 0
	start_index = s.find("[")
	end_index = s.find("]")


	if (ip_check(s)):
		return True
		# s = (s[: start_index] + s[end_index + 1:])


	# if not (ip_check(s)):
	# 	return False
	# else:
	# 	s = (s[: start_index] + s[end_index + 1:])


	while(i < len(s)):
		if( s[i].isdigit() or s[i].isalpha() or s[i] == '.' or s[i] == '-' ):
			# print(i)
			count = count + 1
			i = i + 1
		else:
			i = i + 1

	if (count == len(s) and dot_check(s)):
		return True
	else :
		return False

def char_count_check(s):
	dot_count = s.count(".")
	part = s.split(".")
	i = 0

	if(len(s) > 255):
		return False


	while( i < dot_count):
		if not (len(part[i]) < 64 and len(part[i]) > 0 ):
			return False
		else:
			i = i + 1

	return Trueb

def ip_check(s):b

	start_index = s.find("[")
	end_index = s.find(']')
	isip = False
	switch = True
	i = 0

	# pure_ip를 얻는다
	if(str(start_index).isdigit() and str(end_index).isdigit() and s.count('.') == 3):
		pure_ip = s[start_index + 1 : end_index]
		isip = True
		# return True
	else:
		pure_ip = s
		# return False

	if (isip == True):
		part = pure_ip.split('.')

		while (i < 4):
			if not (part[i].isdigit() and ( int(part[i]) < 256 and int(part[i]) >= 0)):
				return False
			else:
				i = i + 1

		return True


def dot_check(s):
	dot_count = s.count('..')

	if not dot_count > 0 and not (s[0] == '.' or s[-1] == '.') :
		return True
	else:
		return False


def remove_comments(s) : 
    
    start_index = s.find("(")
    end_index = s.find(")")
    
    if(str(start_index).isdigit() and str(end_index).isdigit()):
    	return (s[: start_index] + s[end_index + 1:])
    else:
    	return s

def get_email(message):
	s = input(message)
	s = remove_comments(s)

	if(str(s.find("@")).isdigit()):
		part = s.partition("@")
	else:
		return False

	if (( local_name_check(remove_comments(part[0])) and (domain_check(remove_comments(part[2])))) and char_count_check(part[2])):
		return True
	else:
		return False

	return s


# s = input("message : ")
# print(dot_check(s))
# print(special_str_check(s))
# print("\n\n")
# print(s[0].isdigit())
# print(s[0].isalpha())
# print(special_str_check(s[0]))
# print(s[0] == '.')
# print("\n\n 호스트네임")
# print(local_name_check(remove_comments(s)))
# print("ip체크")
# print(ip_check(s))
# print("도메인체크")
# print(domain_check(remove_comments(s)))
# print("최종")
print(get_email("이메일을 입력해주세요"))




