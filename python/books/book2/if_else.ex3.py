user1=input("enter a number1\n")
user2=input("enter a number2\n")
user3=input("enter a number3\n")
user4=input("enter a number4\n")
user5=input("enter a number5\n")
if user1==user2 or user1==user3 or user1==user4 or user1==user5:
    print user1,"DUPLICATES"
elif user2==user1 or user2==user3 or user2==user4 or user2==user5:
    print user2,"DUPLICATES"
elif user3==user1 or user3==user2 or user3==user4 or user3==user5:
    print user3,"DUPLICATES"
elif user4==user1 or user4==user2 or user4==user3 or user4==user5:
    print user4,"DUPLICATES"
elif user5==user1 or user5==user2 or user5==user3 or user5==user4:
    print user5,"DUPLICATES"
else:
    print "ALL UNIQUE"