store_num=5
count=0
while count<5:
    user=input("enter a number 1 to 10\n")
    if store_num==user:
        print "You are clever You Won"
        break
    elif user<store_num:
        print user,"guess is small"
    elif user>store_num:
        print user,"guess is big"
    else:
        print "You loose Try again"
    count+=1