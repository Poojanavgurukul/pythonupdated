currentUser=["Pooja","Ankita","Deepa","Deepali","Khushboo","Gajal","Shweta"]
newUser=["Kanika","Deepali","Gunjan","SHWETA","Gourav","Priyanka","Ankit"]
for i in newUser:
    if i in currentUser or i in i.upper():
        print "The person will need to enter a new username."
    else:
        print "User name is available"