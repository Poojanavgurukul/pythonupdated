counter =1
while counter<=100:
    value=counter#storing counter value in this variable
    counter2=2
    isPrime=True
    while counter2<value:#till it should be one less from value variable value
        if value%counter2==0:#here it is checking the divisibilty from any factor
            print value,"Is not a prime"
            isPrime=False
            break
        counter2+=1
    if isPrime==True:#is prime value is true than next line will execute
        print value,"Is prime"
    counter+=1