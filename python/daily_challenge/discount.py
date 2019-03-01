user_input=input("enter your quantity\n")
total_cost=user_input*100
if total_cost<1000:
    print "No discount",total_cost
else:
    discount=total_cost*10/100
    total_payment=total_cost-discount
    print "discount",discount
    print "total payment after discount",total_payment