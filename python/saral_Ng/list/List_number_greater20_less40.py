numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
counter=0
element=0
while counter<len(numbers):
    if numbers[counter]>=20 and numbers[counter]<=40:
        element=element+1
    counter+=1
print element