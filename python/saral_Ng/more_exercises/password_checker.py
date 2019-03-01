user_string=raw_input("enter your password\n")
def password_checker(user_string):
    if len(user_string)<6:
        print "password kam se kam 6 character ka hona chahiye usse chota nhi"
        print "weak password"
    elif len(user_string)>16:
        print "password jada se jada 16 character ka hona chahiye usse bada nhi"
        print "weak password"
    elif "$" not in user_string:
        print "password mai kam se kam $ hona chahiye"
        print "weak password"
    elif "2" not in user_string and "8" not in user_string:
        print "password mai 2 ya 8 hona chahiye"
        print "weak password"
    elif "A" not in user_string and "Z" not in user_string:
        print "password mai A ya Z hona chahiye"
        print "weak password"
    else:
        print "strong password"
password_checker(user_string)