user_name=[]
if len(user_name)==0:
    print "We need some users!"
for i in user_name:
    if i=="Admin":
        print "Hello Admin, would you like to see a status report?"
    elif i!="Admin":
        print "Hello",i
        