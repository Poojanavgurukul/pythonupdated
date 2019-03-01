sandwich_orders=["cheese burst","capsicum","chicken","veg","tuna"]
finished_sandwiches=[]
'''i=0
while i<len(sandwich_orders):
    print "I made your",sandwich_orders[i]
    i=i+1
    finished_sandwiches.append(sandwich_orders)
print finished_sandwiches'''
for i in sandwich_orders:
    print "I made your",i
    finished_sandwiches.append(i)
print "i finished this orders",finished_sandwiches