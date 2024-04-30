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
        usr_password = pw.Password_checker(input(prompt))
        usr_password.pattern_search()
    elif usr_input.upper() == "N":
        print("Thank you, Goodbye!")
        break
    else :
        print("Invalid input enter Y or N ")