"2,3,5,7,11,13"
counter=2
isPrime=True
counter2=1
store_value=input("enter a number\n")
while counter<store_value:
    if store_value%counter==0:
        print store_value,"Is Not a prime"     
        isPrime=False
        break
    counter +=1 
if isPrime==True:
    print store_value,"Is Prime"