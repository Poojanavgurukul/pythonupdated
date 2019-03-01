user=[31,3,7,19,21,6,2,15]
counter=0
while counter<len(user)-1:
    counter2=0
    while counter2<len(user)-1:
        if user[counter2]>user[counter2+1]:
            user[counter2],user[counter2+1]=user[counter2+1],user[counter2]
        counter2+=1
    counter+=1
print user