user_inpt=raw_input("enter a number\n")#taking string from user
value=""#empty variable
counter=0#initilize loop
while counter<len(user_inpt):#itll the length of string that user gave
    value+=user_inpt[-counter-1]#it adding the vale in reverse in this variable
    counter+=1
print value