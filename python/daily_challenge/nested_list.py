python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
min,sec_min=float('inf'), float('inf')
counter=0
counter2=0
empty_list=[]
while counter<len(python_students):
    if min>python_students[counter][1]:
        min,sec_min=python_students[counter][1],min
    elif python_students[counter][1]<sec_min:
        sec_min=python_students[counter][1]
    counter+=1
    if sec_min==python_students[counter2][1]:
        empty_list.append(python_students[counter2][0])
        counter2+=1
empty_list.sort()
counter3=0
while counter3<len(empty_list):
    print empty_list[counter3]
    counter3+=1