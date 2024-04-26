# Code to input a grade between 1 and 100 and display the exam grade according to a set of rules
#---------------------------------

#---------------------
# functions
#---------------------
def int_error_checker(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
            break
        except ValueError:
            print("Wrong type of value, please enter a number")
        



#-------------------------
# Main body
#-------------------------

# User input 
while True:
    grade = int_error_checker("What grade did you achieve?:")
    if 0 < grade <= 100:
        if 0 < grade < 50:
            print( "Fail")
        elif 50 <= grade < 61:
            print("Pass")
        elif 60 < grade <= 70:
            print("Merit")
        elif 70 < grade <= 100:
            print("Distinction")
        break
    else:
       print("wrong input try again!:")

