ar=[18 ,90 ,90 ,13, 90, 75, 90, 8, 90, 43]
max=ar[0]
sum=0
counter=0
while counter<len(ar):
    if max<=ar[counter]:
        max=ar[counter]
    counter+=1
for i in ar:
    if max==i:
        sum+=1
print sum