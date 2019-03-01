user1=input("enter a number1\n")
user2=input("enter a number2\n")
user3=input("enter a number3\n")
user4=input("enter a number4\n")
user5=input("enter a number5\n")
if user1>=user2 and user1>=user3 and user1>=user4 and user1>=user5:
    print "max",user1
elif user2>=user1 and user2>=user3 and user2>=user4 and user2>=user5:
    print "max",user2
elif user3>=user1 and user3>=user3 and user3>=user4 and user3>=user5:
    print "max",user3
elif user1<=user2 and user2<=user3 and user3<=user4 and user4>=user5:
    print "max",user4
else:
    print "max",user5
if user1<=user2 and user1<=user3 and user1<=user4 and user1<=user5:
    print "min",user1
elif user2<=user1 and user2<=user3 and user2<=user4 and user2<=user5:
    print "min",user2
elif user3<=user1 and user3<=user2 and user3<=user4 and user3<=user5:
    print "min",user3
elif user4<=user1 and user4<=user2 and user4<=user3 and user4<=user5:
    print "min",user4
else:
    print "min",user5
#2, 4 2, 3 and 3,
#3, 2, 5, 0, 1