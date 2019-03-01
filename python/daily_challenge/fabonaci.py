a=0
b=1
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
counter=0
while counter<=10:
    if counter<=1:
       next=counter
       print next
    else:
        next=a+b
        a=b
        b=next
        print next
    counter+=1