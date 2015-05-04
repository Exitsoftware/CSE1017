#coding: utf-8

def one_sentence_per_line(filename) :
    infile = open(filename,"r")
    outfile = open("result2.txt","w")
    text=infile.read()
    index= text.find(".")
    index2=text.find("?")
 
    count=0
    while index != -1 or index2 != -1:
        
        if index!=-1 :
            index= text.find(".",index+1)
            count=count+1
            t=text.partition(".")
            text=t[2]
            outfile.write(t[0].lstrip()+".\n")
            
        elif index2!=-1 :
            index2= text.find("?",index2+1)
            count=count+1
            t=text.partition("?")
            text=t[2]
            outfile.write(t[0].lstrip()+"?\n")
             

    outfile.write("문장이 총"+str(count)+"개\n")
    infile.close()
    outfile.close()

one_sentence_per_line("article.txt")