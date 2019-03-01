marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
    ]                      
counter=0
while counter<len(marks):
    counter2=0
    sum1=0
    while counter2<len(marks[counter]):
        length=len(marks[counter])
        sum1+=marks[counter][counter2]
        average=sum1/length
        counter2+=1
    counter+=1
    print (average)