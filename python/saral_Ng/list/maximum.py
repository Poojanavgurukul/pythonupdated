numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=numbers[0]
counter=0
while counter<len(numbers):
    if max<=numbers[counter]:
        max=numbers[counter]
    counter+=1
print max