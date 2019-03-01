main_list=[[1,2,3], [4,5,6], [10,11,12], [7,8,9],[23,45,89,78]]
empty_list=[]
counter=0
while counter<len(main_list):
    counter2=0
    sum=0
    while counter2<len(main_list[counter]):
        sum+=main_list[counter][counter2]
        counter2+=1
    empty_list.append(sum)
    counter+=1
counter3=0
max=0
while counter3<len(empty_list):
    if  max<empty_list[counter3]:
        max=empty_list[counter3]
        count=counter3
    counter3+=1
print main_list[count]