list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
notInlist2=[]
counter=0
while counter<len(list1):
        if (list1[counter]) not in list2:
            notInlist2.append(list1[counter])
        counter+=1
print (notInlist2)