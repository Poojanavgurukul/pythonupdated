n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
empty_list=[]
counter=0
while counter<len(n):
    if n[counter] not in empty_list:
        empty_list.append(n[counter])
    counter+=1
print empty_list