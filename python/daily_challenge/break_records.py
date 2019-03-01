scores=[10 ,5 ,20, 20, 4, 5 ,2 ,25 ,1]
max=scores[0]
sum=0
counter=0
while counter<len(scores):
    if max<scores[counter]:
        max=scores[counter]
        print max
        sum+=1
    counter+=1
print sum