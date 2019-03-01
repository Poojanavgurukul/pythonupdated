char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
empty_list=[]
counter=0
occurance_list=[]
while counter<len(char_list):
    if char_list[counter] in empty_list:
        counter+=1
    else:
        empty_list.append(char_list[counter])
        counter2=0
        occur=0
        while counter2<len(char_list):
            if char_list[counter2] == char_list[counter]:
                occur+=1
            counter2+=1
        if char_list[counter] not in occurance_list:
            occurance_list.append([char_list[counter],occur])
    counter+=1
print occurance_list