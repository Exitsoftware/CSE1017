#coding: utf-8


def one_sentence_per_line(filename) : 
	
	count = 0
	sentence_count = 0 
	infile = open(filename,"r") 
	outfile = open("result2.txt","w") 
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
			outfile.write("문장은 " + str(sentence_count) + "개 입니다.\n")
			print("done")
			exit()

		sentence = text[start_index : last_index + 1 ]
		sentence_count = sentence_count + 1
		sentence = sentence.strip()
		outfile.write(sentence + "\n\n")


		start_index = last_index + 1

	outfile.write("\n\n문장은 " + str(sentence_count) + "개 입니다.\n")
	infile.close() 
	outfile.close() 
	print("done")

one_sentence_per_line("article.txt")