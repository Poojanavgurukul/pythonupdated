user=input("enter a number\n")
factorial=1
count=1
if user==0:
    factorial=0
while count<=user:
    factorial=factorial*count
    count=count+1
print factorial