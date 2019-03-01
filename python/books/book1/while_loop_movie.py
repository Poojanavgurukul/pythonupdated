numberOfPerson=input("enter how many member you are???\n")
i=0
while i <numberOfPerson:
    userAge=input("enter your age ??\n")
    if userAge<=3:
        print "free"
    elif userAge>=3 and userAge<=12:
        print "cost $10"
    elif userAge>12:
        print "cost $15"
    i+=1
