def divisibleby3_7():
    counter=1
    while counter<=1000:
        if counter%3==0:
            print counter,"nav"
            if counter%21==0:
                print counter,"navgurukul"
        elif counter%7==0:
            print counter,"gurukul"
        counter+=1
divisibleby3_7()