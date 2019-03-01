numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
maxNumber=0
second_max=0
counter=0
while counter<len(numbers):
    if maxNumber<numbers[counter]:
        maxNumber=numbers[counter]
    if numbers[counter]<maxNumber and second_max<numbers[counter]:
        second_max=numbers[counter]
    counter+=1
print "Second max number:"+str(second_max)