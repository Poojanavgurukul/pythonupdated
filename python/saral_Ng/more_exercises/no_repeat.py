def no_repeat(string):
    new_list=[]
    counter=0
    while counter<len(string):
        if string[counter] not in new_list:
            new_list.append(string[counter])
        counter+=1
    print new_list
no_repeat(["Rishabh","Rishabh","Abhishek","Divyanshu","Divyanshu"])