list=[[2,0,4,5],
      [5,6,0,3],
      [0,1,8,9],
      [9,7,6,0]]
counter=0
sum=0
while counter<len(list):
    length=len(list[counter])-1
    counter2=0
    while counter2<len(list[counter]):
        if counter2 ==0 and list[counter2+1][counter] !=0:
            sum=sum+list[counter2][counter]
        if counter2 == len(list[counter])-1 and list[counter2-1][counter]!=0:
            sum=sum+list[counter2][counter]
        if counter2!=0 and counter2!=length:
            if list[counter2-1][counter]!=0 and list[counter2+1][counter]!=0:
                sum=sum+list[counter2][counter]
        counter2+=1
    counter+=1
print sum

"""lists=[[2,0,4,5],
      [5,6,0,3],
      [0,1,8,9],
      [9,7,6,0]]
count = 0
while count < len(lists):
    counter = 0
    sum = 0
    while counter < len(lists[count]):
        if lists[count][counter] == 0:
            lists.remove([count-1][counter])
            lists.remove([count+1][counter])
            sum = sum+int([count][counter])
            count+=1
        counter+=1
    count+=1
    print sum"""