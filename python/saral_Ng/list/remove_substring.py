mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on"
new_list=[]
word=""
counter=0
counter2=0
while counter<len(mainStr):
    if mainStr[counter] !=" ":
        word+=mainStr[counter]
    elif mainStr[counter] == " ":
        new_list.append(word)
        word=""
    counter+=1  
if word != "":
    new_list.append(word)    
while counter2<len(new_list):
    """if new_list[counter2]!=subStr:
        accurate_list.append(new_list[counter2])"""
    if new_list[counter2] ==subStr:
        new_list[counter2]=replacementStr
    print new_list[counter2],
    counter2+=1