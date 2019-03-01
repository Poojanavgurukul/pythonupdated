a=0
b=1
count=0
while count<100:
    if count<=1:
         next=count
    else:
        next=a+b
        a=b
        b=next
    print next
    count+=1