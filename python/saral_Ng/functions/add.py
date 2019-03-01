def add(num1,num2):
    print "sum of both numbers is",num1+num2
add(56,12)
def add_list_number(number_list1,number_list2):
    counter=0
    while counter<len(number_list1):
        print number_list1[counter]+number_list2[counter]
        print "............."
        counter+=1
add_list_number([50, 60, 10],[10, 20, 13])