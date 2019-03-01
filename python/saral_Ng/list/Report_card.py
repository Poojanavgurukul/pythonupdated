marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
    ]
sum =0
counter=0
while counter<len(marks):
    counter2=0
    while counter2<len(marks[counter]):
        sum=sum+marks[counter][counter2]
        counter2+=1
    counter+=1
print (sum)