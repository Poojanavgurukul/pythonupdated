user_input=int(raw_input("enter a number\n"))
if user_input<1:
    print "paani bharna hai"
elif user_input>1 and user_input<=10:
    print "aur nahi bharna"
else:
    print "paani overflow ho rha hai"