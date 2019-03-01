number_x=int(raw_input("enter a number\n"))
number_y=int(raw_input("enter a number\n"))
def calculator(number_x,number_y ,operation):
    if operation=="add":
        return "add",number_x+number_y
    elif operation=="multiply":
        return "multiply",number_x*number_y
    elif operation=="divide":
        return "divide",number_x/number_y
    elif operation=="subtract":
        return "subtract",number_x-number_y
add_result=calculator(number_x,number_y,"add")
subtract_result= calculator(number_x,number_y,"subtract") 
multiply_result= calculator(number_x,number_y,"multiply")
divide_result= calculator(number_x,number_y,"divide")
print add_result
print multiply_result
print divide_result
print subtract_result

print "...................."

def list_change(integer_list1,integer_list2):
    counter=0
    multiply_list=[]
    while counter<len(integer_list1):
        result=integer_list1[counter]*integer_list2[counter]
        multiply_list.append(result)
        counter+=1
    return multiply_list
multiple_list_new = list_change([5, 10, 50, 20], [2, 20, 3, 5])
print multiple_list_new