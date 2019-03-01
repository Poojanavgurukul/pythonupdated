def even_numbers(num1,num2):
    if num1%2==0 and num2%2==0:
        print "Dono even hai"
    else:
        print "Dono even nahi hai"
even_numbers(12,31)
print "............"
def even_numbers_list(numbers_list1,numbers_list2):
    counter=0
    while counter<len(numbers_list1):
        if numbers_list1[counter]%2==0 and numbers_list2[counter]%2==0:
            print "Dono even hai"
        else:
            print "Dono even nahi hai"
        counter+=1
even_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])