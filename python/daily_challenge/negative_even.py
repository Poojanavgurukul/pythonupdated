list=[1,2,3,-1,-2,-3,4,5,-4,-5,9]
positive_even=0
negative_even=0
positive_odd=0
negative_odd=0
counter=0
while counter<len(list):
    if list[counter]<0:
        if list[counter]%2==0:
            negative_even+=1
        else:
            negative_odd+=1
    else:
        if list[counter]%2==0:
            positive_even+=1
        else:
            positive_odd+=1
    counter+=1
print "negative even",negative_even
print "positive even",positive_even
print "negative odd",negative_odd
print "positive odd",positive_odd