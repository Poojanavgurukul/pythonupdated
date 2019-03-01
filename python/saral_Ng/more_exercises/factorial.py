number_input=input("enter a number\n")
def factorial(number_input):
    
    factorial=1
    if number_input==0:
            factorial=0
    elif number_input==1:
        factorial=1
    else:
        counter=1
        while counter<=number_input:
            factorial=factorial*counter
            counter+=1
    print factorial
factorial(number_input)