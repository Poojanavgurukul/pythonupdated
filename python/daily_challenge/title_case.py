str = 'lEaRn pYtHoN'
word=""
empty_list=[]
counter=0
while counter<len(str):
    if str[counter]!=" ":
        word+=str[counter].lower()
    elif str[counter] == " ":
        empty_list.append(word)
        word=""
    counter+=1
if word !="":
    empty_list.append(word)
counter2=0
while counter2<len(empty_list):
    counter3=0
    word1=""
    sum=""
    while counter3<len(empty_list[counter2]):
        if empty_list[counter2][counter3] == empty_list[0][0] or empty_list[counter2][counter3]==empty_list[1][0]:
            word1+=empty_list[counter2][counter3].upper()
        else:
            sum+=empty_list[counter2][counter3]
        counter3+=1
    counter2+=1
    print word1+sum,