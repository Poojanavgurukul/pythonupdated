counter=1
while counter<=100:
    if counter%3==0 and counter%7==0:
        print "NavGurukul"
    elif counter%3==0:
        print "Nav"
    elif counter%7==0:
        print "Gururkul" 
    else:
        print counter
    counter+=1