#coding: utf-8


def one_sentence_per_line(filename,key) : 
	
	count = 0
	sentence_count = 0 
	infile = open(filename,"r") 
	outfile = open("result2.txt","w") 
	text = infile.read() 
	start_index = 0
	last_index = text.find(".")

	while not (last_index == -1):

		islast = False
		

		# last_index = text.find(".", start_index)
		
		if (( text.find(".", start_index) <= text.find("?", start_index))) or text.find("?", start_index) == -1 :
			last_index = text.find(".", start_index)
			# print(last_index)
		elif ((text.find(".", start_index) >= text.find("?", start_index))) or text.find(".", start_index) == -1:
			last_index = text.find("?", start_index)

		if(last_index == -1):
			outfile.write("문장은 " + str(sentence_count) + "개 입니다.\n")
			print("done")
			exit()

		sentence = text[start_index : last_index + 1 ]
		sentence_count = sentence_count + 1
		sentence = sentence.strip()
		outfile.write(sentence + "\n\n")

		word_index = sentence.find(key)

		# if( word_index == -1):
		# 	outfile.write(key + "는 해당 문장에 없습니다.\n")
		# 	# print("done")
		# else:
		# 	word_index2 = sentence.find(key,word_index+1) 

		# 	while not (islast):
		# 	    if( word_index2 == -1):
		# 	    	# outfile.write(key + "의 위치번호는 " + str(word_index) + "\n") 
		# 	    	count = count + 1
		# 	    	islast = True
		# 	    else:
		# 	    	count = count + 1
		# 	    	word_index = word_index2
		# 	    	word_index2 = sentence.find(key, word_index+1)

		#     # outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
		# 	outfile.write(key + "는 " + str(count) + "번 나옵니다\n")
		# 	count = 0



		# if( word_index == -1):
		# 	outfile.write(key + "는 해당 문장에 없습니다.")
		# 	# print("done")

		# word_index2 = sentence.find(key,word_index+1) 

		# while not (islast):
		#     if( word_index2 == -1):
		#     	# outfile.write(key + "의 위치번호는 " + str(word_index) + "\n") 
		#     	count = count + 1
		#     	islast = True
		#     else:
		#     	count = count + 1
		#     	word_index = word_index2
		#     	word_index2 = sentence.find(key, word_index+1)

	 #    # outfile.write(key + "의 위치번호는 " + str(pos) + "\n") 
		# outfile.write(key + "는 " + str(count) + "번 나옵니다\n")

		start_index = last_index + 1

	outfile.write("\n\n문장은 " + str(sentence_count) + "개 입니다.\n")
	infile.close() 
	outfile.close() 
	print("done")

s = input("찾을 문자열입력해주세요.")
# find_second("article.txt", s)
one_sentence_per_line("article.txt", s)