question_list = [
	"How many continents are there?",  			
	"What is the capital of India?",			
	"NG mei kaun se course padhaya jaata hai?"	
]

options_list = [
	["Four", "Nine", "Seven", "Eight"],
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

solution_list = [3, 4, 1]
price_money=[1000,5000,10000]
counter=0
while counter<len(question_list):
    print question_list[counter]
    Answer=solution_list[counter]
    price=price_money[counter]
    counter2=0
    count=1
    while counter2<len(options_list[counter]):
        print count,options_list[counter][counter2]
        counter2+=1
        count+=1
    counter+=1
    life_line5050=raw_input("kya aap life line use karna chate ho:yes/no\n")
    if life_line5050=="no":
        user_input=input("enter your answer\n")
        if user_input==Answer:
            print "Congrats! Aapka answer sahi hai"
            print "Aap",price,"jeet chuke hai"
        else:
            print "Sadly aapka javab galat hai"
            print "Aap Game se bhar ho gye hai"
            break
    elif life_line5050=="yes":
        print counter+1,options_list[counter][counter]
        print solution_list[counter],options_list[counter][solution_list[counter]-1]