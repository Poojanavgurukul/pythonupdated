elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
total_even=0
total_odd=0
while counter<len(elements):
    if elements[counter]%2==0:
        total_even+=1
    else:
        total_odd+=1
    counter+=1
print "even number",total_even
print "odd number",total_odd