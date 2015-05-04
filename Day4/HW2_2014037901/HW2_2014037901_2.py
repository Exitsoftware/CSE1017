#coding: utf-8


def one_sentence_per_line(filename,key) : 
	
	count = 0
	sentence_count = 0 
	total_count = 0
	line_count = 0
	infile = open(filename,"r") 
	outfile = open("result3.txt","w") 
	text = infile.read() 
	start_index = 0
	last_index = text.find(".")

	while not (last_index == -1):

		islast = False
		
		if (( text.find(".", start_index) <= text.find("?", start_index))) or text.find("?", start_index) == -1 :
			last_index = text.find(".", start_index)

		elif ((text.find(".", start_index) >= text.find("?", start_index))) or text.find(".", start_index) == -1:
			last_index = text.find("?", start_index)

		if(last_index == -1):
			outfile.write(key + "는 " + str(line_count) + "개 문장에서 " + str(total_count) + "번 나옵니다\n\n")
			print("done")
			exit()

		sentence = text[start_index : last_index + 1 ]
		sentence_count = sentence_count + 1
		sentence = sentence.strip()

		word_index = sentence.find(key)

		if not ( word_index == -1):
			line_count = line_count + 1
			outfile.write(sentence + "\n")
			word_index2 = sentence.find(key,word_index+1) 

			while not (islast):
				if( word_index2 == -1):
					count = count + 1
					total_count = total_count + 1
					islast = True
				else:
					count = count + 1
					total_count = total_count +1
					word_index = word_index2
					word_index2 = sentence.find(key, word_index+1)

			outfile.write(key + "는 " + str(count) + "번 나옵니다\n\n")
			count = 0


		start_index = last_index + 1

	outfile.write(key + "는 " + str(line_count) + "개 문장에서 " + str(total_count) + "번 나옵니다\n\n")
	infile.close() 
	outfile.close() 
	print("done")

s = input("찾을 문자열입력해주세요.")
one_sentence_per_line("article.txt", s)