i=1
sum=0
list_number=[]
min=0
while i<=20:
    user=float(raw_input("enter a decimal numbers\n"))
    list_number.append(user)
    sum+=user
    i=i+1
    average=sum/20.0
    maxnum=list_number[0]
    minnum=list_number[0]
    for j in list_number:
        for k in list_number:
            if j>k and j>maxnum:
                maxnum=j
            else:
                if j<k and j<minnum:
                    minnum=j
print sum
print average
print maxnum
print minnum
