def check_user_name(s) :
	if not check_dot(s) :
		return False
	for i in s :
		if i.isalpha() or i.isdigit() or check_special(i) :
			return True
		else :
			return False

def check_special(s) :
	special_list1 = ["!","#","$","%","&","'","*","+","_","/","=","?","^","_","{","|","}","`","."]
	if s in special_list1 :
		return True
	else :
		return False

def check_dot(s) :
	if s.startswith(".") or s.endswith(".") or (".." in s) :
		return False
	else : 
		return True

def remove_comment(s) :
	if "(" in s :
	    a = s.find("(")
	    b = s.find(")")
	    s2 = s[:a] + s[b+1:]
	    return s2
	else :
		return s

def check_domain(s) :
	if s.startswith("[") and s.endswith("]") and check_IP(s[1:-1]) :
		return True
	elif not check_dot(s) :
		return False
	else :
		for i in s :
			if i.isdigit() or i.isalpha() or i == "-" or i == "." :
				return True
			else :
				return False

def check_IP(s) :
	for i in s :
		if i.isdigit() or i == "." :
			return True
		else :
			return False

def get_email(message) :
	s = input(message)
	(name, mid, address) = s.partition("@")
	name=remove_comment(name)
	address=remove_comment(address)
	while not (check_user_name(name) and mid == "@" and check_domain(address)) :
		s = input(message)
		(name, mid, address) = s.partition("@")
		name=remove_comment(name)
		address=remove_comment(address)
	s=name+mid+address
	return s

print (get_email("이메일을 입력해주세요"))