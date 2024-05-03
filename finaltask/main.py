'''
This file is the main file from which my password checker is run.
Technically It could just all go into one file if wer're being honest.
'''
import password_checker as pw


MENU = '''
Welcome to the password checker!
Either enter your password to check its strength.\n
'''

#--------------------------------------------------------------------
# This While loop executes the menu in which the user interacts with
# Also execures the methods from the password checker class
#--------------------------------------------------------------------
while True:
    usr_input = input("Would you like to check your password (Y/N)")
    if usr_input.upper() == "Y":
        print(MENU)
        PROMPT = "Please enter a password to check its strength: "
        usr_input = input(PROMPT)

        if usr_input not in pw.Password_checker.very_weak_passwords:
            usr_password = pw.Password_checker(usr_input)
            usr_password.pass_rank(
                usr_password.how_many_special_characters(),
                usr_password.length_rating(),
                usr_password.pattern_search())
        else: print("This is a VERY WEAK PASSWORD")
    elif usr_input.upper() == "N":
        print("Thank you, Goodbye!")
        break
    else :
        print("Invalid input enter Y or N ")
