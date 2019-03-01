list=[10, 32, 42, 65, 67, 89, 76, 38, 67,-9,2]
min,sec_min=float('inf'), float('inf')
counter=0
while counter<len(list):
    if min>list[counter]:
        min,sec_min=list[counter],min
    elif list[counter]<sec_min:
        sec_min=list[counter]
    counter+=1
print min,sec_min