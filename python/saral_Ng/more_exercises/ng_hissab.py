student_user=int(raw_input("enter a numbers of student\n"))
money_per_student_user=int(raw_input("enter a amount of money per student\n"))
def kharcha(student_user,money_per_student_user):
    total_kharcha=student_user*money_per_student_user
    if total_kharcha<=50000:
        print "Hum budget ke andar hain"
    else:
        print  "hum budget ke bahar hain."
kharcha(student_user,money_per_student_user)