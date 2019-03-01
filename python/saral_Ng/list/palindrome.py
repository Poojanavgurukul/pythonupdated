name=[ 'n', 'i', 't', 'i', 'n' ]
reverse_name=[]
i=0
while i<len(name):
    reverse_name.append(name[-i-1])
    i+=1
if name==reverse_name:
    print "Palindrome hai"
else:
    print "Palindrome nahi hai"