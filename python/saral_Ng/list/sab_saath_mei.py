elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
total_count_even=0
total_count_odd=0
total_even=0
total_odd=0
while counter<len(elements):
    if elements[counter]%2==0:
        total_count_even+=1
        total_even+=elements[counter]
        print elements[counter],"is even number ka count hai",total_count_even
        print "sum of",total_count_even,"even numbers is",total_even
        average_even=total_even/total_count_even
        print total_even,"ka average hai",average_even
    else:
        total_count_odd+=1
        total_odd+=elements[counter]
        print elements[counter],"is odd number ka count hai",total_count_odd
        print "sum of",total_count_odd,"odd numbers is",total_odd
        average_odd=total_odd/total_count_odd
        print total_odd,"ka average hai",average_odd
    counter+=1
average_even=total_even/total_count_even
average_odd=total_odd/total_count_odd
print "even total number",total_count_even
print "odd total number",total_count_odd  
print "total sum of even",total_even
print "total sum of odd",total_odd
print "total even number ka average hai",average_even
print "total odd number ka average hai",average_odd  