string ="This is my code"
word=""
counter=0
while counter<len(string):  
    if string[-counter-1] !=" ":
        word+=string[-counter-1]
    elif string[-counter-1]==" ":
        print word,
        word=""
    counter+=1
if word !="":
    print word,
counter2=0