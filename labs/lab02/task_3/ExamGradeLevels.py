# Code to input a grade between 1 and 100 and display the exam grade according to a set of rules
#---------------------------------

import sys
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
levels = 1, 2
# User input 
while True:
    grade = int_error_checker("What grade did you achieve?:")
    level = int_error_checker("What level are you?: ")

    while True:
        if level == levels[0]:
            if 0 < grade <= 100:
                if 0 < grade < 50:
                    print( "Fail")
                elif 50 <= grade < 61:
                    print("Pass")
                elif 60 < grade <= 70:
                    print("Merit")
                elif 70 < grade <= 100:
                    print("Distinction")
                sys.exit()
            else:
                print("wrong input try again!:")

        elif level == levels[1]:
            if 0 < grade <= 100:
                if 0 < grade < 40:
                    print( "Fail")
                elif 39 <= grade < 51:
                    print("Pass")
                elif 50 < grade <= 65:
                    print("Merit")
                elif 65 < grade <= 100:
                    print("Distinction")
                sys.exit()


