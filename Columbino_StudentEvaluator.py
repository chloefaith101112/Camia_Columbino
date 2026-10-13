

name = " "
a1 =  0
a2 =  0
a3 =  0
average = 0
level = " "

def display_header():
    print ("=======================================")
    print ("STUDENT PERFORMANCE EVALUATOR")
    print("=======================================")
    print (" ")

def get_student_info():
    name = input("Enter student name: ")
    a1 = input("Enter student Assessment 1: ")
    a2 = input("Enter student Assessment 2: ")
    a3 = input("Enter student Assessment 3: ")
    return name, a1, a2, a3


def evaluate_performance() :
    average = (a1 + a2 + a3) / 3
    if 90 < average < 100:
        level = ("Outstanding")
    elif 85 < average < 89:
        level = ("Very Satisfactory")
    elif 80 < average < 84:
        level = ("Satisfactory")
    elif 75 < average < 79:
        level = ("Fairly Satisfactory")
    else:
        level = ("Needs Improvement")
    return level, average

def display_report() :
    print("=======================================")
    print("STUDENT PERFORMANCE REPORT")
    print("=======================================")
    print(f"Student Name:  {name}")
    print(f"Assessment Scores:  {a1, a2, a3}")
    print(f"Average Score:  {average:.2f}")
    print(f"Performance Level:  {level}" )





display_header()
get_student_info()
evaluate_performance()
display_report()



















