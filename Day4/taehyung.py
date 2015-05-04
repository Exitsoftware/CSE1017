#coding: utf-8
def find_all_sentence(filename,key) :
   infile = open(filename,"r")
   outfile = open("result2.txt","w")
   text = infile.read()
   
   a = 0 #문장갯수를 세는 변수
   b = text.count(key) 
   s = text.split(".")
   

   for i in s: 
      if i.find(key) != -1 : 
         d = i.count(key)
         outfile.write(str(key)+"이(가)"+ str(d) +"번 등장\n"+str(i)+"\n")
         a = a + 1
      
   outfile.write(key + "이(가)" + str(a) + "개 문장에서" + str(b) + "번 등장")
   infile.close()
   outfile.close()
   print("done")
   exit()


find_all_sentence("article.txt","컴퓨터")