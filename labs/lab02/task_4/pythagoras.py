'''
In this lab you'll write a program that calculates the lengths of sides of a triangle using Pythagoras’s Theorem. 

Pythagoras’ Theorem states that the square of the long side (C) of a right-angled triangle is the sum of the squares of the two shorter sides (A and B).  
	C**2 = A**2 + B**2

'''
import math
#-----------------
# FUNCTIONS
#-----------------
def usr_input(prompt):
    '''prompts user for a valid character of either 1,2,3 or A, B C.
    
    Return:
        int: if 1,2,3
        or 
        str: if A,B,C 
    '''
    while True:
        valid_char = "123ABC" 
        try:
            value = input(prompt)
            if value.upper() in valid_char:
                 if value.isdigit():    # check if digit is numeric
                      return int(value)
                 else:
                    return value.upper()   # Return uppercase string     
            else: 
                print("Wrong input, try again!")
        except ValueError:
                print("Wrong input try again!:")

def int_verify(length_prompt):
    value = input(length_prompt)
    while True:
        if value.isdigit():
            return(int(value))
        else: 
             print("Input must be a number try again!:")
        




def Pythagoras_calc(A=0,B=0,C=0):
    ''' Takes user values, using pythagoras to calculate length of sides
    
    Return:
        int: value of missing side
    '''
    # Asq Bsq = Csq
    #length_A = int_verify("what is the length of B: ")
    #length_B = int_verify("what is the length of B: ")
    #length_C = int_verify("what is the length of C: ")
    if A == 0:
        A = math.sqrt((C**2 - B**2))
        value = A
    elif B == 0:
        B = math.sqrt((C**2 - A**2))
        value = B
    else:
        C = math.sqrt((A**2 + B**2))
        value = C
    return value


    


#----------------
# variables
#----------------
prompt = 'Which option do you want?:\n'
#usr_option = input(prompt)
menu = '''
Pythagoras' Calculator\n
 Find the length of A given B and C     option:1
 Find the length of B given A and C     option:2
 Find the length of C given A and B     option:3
'''


#++++++++++++++++++
# Print a menu
#++++++++++++++++++
while True:
    print(menu)
    usr_option = usr_input(prompt)  # selecting which calculation
    if usr_option == 1:
        print("Calculating A")
        length_B = int_verify("what is the length of B: ")
        length_C = int_verify("what is the length of C: ")
        print(Pythagoras_calc(0,length_B,length_C))
    elif usr_option ==2:
        length_A = int_verify("what is the length of A: ")
        length_C = int_verify("what is the length of C: ")
        print(Pythagoras_calc(length_A,0,length_C))
    elif usr_option ==3:
        length_A = int_verify("what is the length of A: ")
        length_B = int_verify("what is the length of B: ")
        print(Pythagoras_calc(length_A,length_B,0))
    else:
        print("Wrong input we need either a 1,2, or 3:\n")

