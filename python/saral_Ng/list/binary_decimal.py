binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
i=0
IsValidList=True
Decimal_value=0
while i<len(binary_number):
    if binary_number[i]!=1 and binary_number[i]!=0:
        IsValidList=False
        print "Inavlid List"
        break
    else:
        Decimal_value+=int(binary_number[-i-1])*2**i
    i+=1
if IsValidList==True:
    print Decimal_value