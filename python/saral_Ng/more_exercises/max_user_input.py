num1=int(raw_input("enter number1\n"))
num2=int(raw_input("enter number2\n"))
num3=int(raw_input("enter number3\n"))
def max(num1,num2,num3):
    if num1>num2>num3:
        print num1
    elif num1<num2>num3:
        print num2
    elif num1<num2<num3:
        print num3
max(num1,num2,num3)