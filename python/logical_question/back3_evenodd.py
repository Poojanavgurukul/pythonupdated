user=input("enter a number\n")
i=user
j=user
while i<=user+10:
	if i%2 !=0:
		print i,"odd"
		if i==user+5:
			break
	else:
		if j%2==0:
			print j,"even"
		if j==user-5:
			break
	i=i+1
	j=j-1
