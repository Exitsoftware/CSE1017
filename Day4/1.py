#coding: utf-8

def find_first(filename,key) : 
    infile = open(filename,"r") 
    outfile = open("result.txt","w") 
    text = infile.read() 
    pos = text.find(key) 
    outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
    infile.close() 
    outfile.close() 
    print("done")

def find_second(filename,key) : 
    infile = open(filename,"r") 
    outfile = open("result.txt","a+") 
    text = infile.read() 
    pos = text.find(key) 
    pos = text.find(key,pos+1) 
    outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
    infile.close() 
    outfile.close() 
    print("done")

def find_second(filename,key) : 
	islast = False
	infile = open(filename,"r") 
	outfile = open("result.txt","a+") 
	text = infile.read() 
	pos = text.find(key) 
	if( pos == -1):
		outfile.write(key + "는 해당파일에 없습니다.")
		print("done")
		exit()
	pos2 = text.find(key,pos+1) 

	while not (islast):
	    if( pos2 == -1):
	    	outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
	    	islast = True
	    else:
	    	pos = pos2
	    	pos2 = text.find(key, pos+1)

    # outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
	infile.close() 
	outfile.close() 
	print("done")

def find_all(filename,key) : 
	count = 0
	islast = False
	infile = open(filename,"r") 
	outfile = open("result.txt","a+") 
	text = infile.read() 
	pos = text.find(key) 
	if( pos == -1):
		outfile.write(key + "는 해당파일에 없습니다.")
		print("done")
		exit()
	pos2 = text.find(key,pos+1) 

	while not (islast):
	    if( pos2 == -1):
	    	count = count + 1
	    	outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
	    	islast = True
	    else:
	    	count = count + 1
	    	outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
	    	pos = pos2
	    	pos2 = text.find(key, pos+1)

    # outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
	outfile.write(key + "는 " + str(count) + "번 나옵니다\n") 
	infile.close() 
	outfile.close() 
	print("done")

def text_count(filename,key) : 
	islast = False
	count = 0
	infile = open(filename,"r") 
	outfile = open("result.txt","a+") 
	text = infile.read() 
	pos = text.find(key) 
	if( pos == -1):
		outfile.write(key + "는 해당파일에 없습니다.")
		print("done")
		exit()
	pos2 = text.find(key,pos+1) 

	while not (islast):
	    if( pos2 == -1):
	    	# outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
	    	count = count + 1
	    	islast = True
	    else:
	    	count = count + 1
	    	pos = pos2
	    	pos2 = text.find(key, pos+1)

    # outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
	outfile.write(key + "는 " + str(count) + "번 나옵니다\n") 
	infile.close() 
	outfile.close() 
	print("done")

s = input("찾을 문자열입력해주세요.")
# find_second("article.txt", s)
find_all("article.txt", s)