import password_checker as pw


menu = '''
Welcome to the password checker!
Either enter your password to check its strength.\n
'''
while True: 
    usr_input = input("Would you like to check your password (Y/N)")
    if usr_input.upper() == "Y":
        print(menu)
        prompt = "Please enter a password to check its strength: "
        usr_input = input(prompt)

        if usr_input not in pw.Password_checker.very_weak_passwords:
            usr_password = pw.Password_checker(usr_input)
            
            usr_password.pass_rank(usr_password.how_many_special_characters(),usr_password.length_rating(),usr_password.pattern_search())
        else:
            print("This is a VERY WEAK PASSWORD")
    elif usr_input.upper() == "N":
        print("Thank you, Goodbye!")
        break
    else :
        print("Invalid input enter Y or N ")