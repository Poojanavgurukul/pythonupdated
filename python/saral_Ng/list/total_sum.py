n=[10,11,12,13,14,17,18,19]
sum=n[0]
sum2=n[1]
counter=0
b=[]
numbers=30
while counter<len(n):
    counter2=1
    while counter2<len(n):
        sum=n[counter]
        sum2=n[counter2]
        c=sum
        d=sum2
        if numbers==sum+sum2:
            var= [c,d]
            if sorted(var) not in b:
                b.append([c,d])
        counter2+=1
    counter+=1
print (b)