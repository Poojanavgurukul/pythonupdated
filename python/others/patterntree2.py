user=input("enter a odd number\n")#
star1=1#
space1=user/2#
while star1<=user:
    if star1%2 !=0:#
        print space1*" ",star1*"*"
    star1=star1+1#
    if star1%2==0:#
        space1=space1-1#
star2=user-2#
space2=1#
while star2>0:
    if star2%2 !=0:#
        print space2*" ",star2*"*"
    star2-=1 #
    if star2%2==0:#
        space2+=1#