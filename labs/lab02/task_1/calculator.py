# Create a calculator 

# Requesting User input
usr_input = [int(input("First number")), int(input("Second Number"))]

#--------------------------
# Useful functions
#--------------------------

def error_handling(prompt,compare):
    while True:
        if prompt in compare:
            break
        else:
            print("wrong input try again!:")
    return prompt

#--------------------------
# Calculator menu
#--------------------------

while True:
    print('''
        Add \t\t +\n
        Subtract \t -\n
        Multiply\t\t *\n
        Divide\t\t / \n
        Square\t\t s \n    
          ''')

    # list of operations 
    operations = "+", "-", "*", "/", "s"
    # Ask user what operation they want to perform.
    # Error handling

    usr_operation = error_handling(input("From the menu which operation do you want to perform?:\n"),operations)
    if usr_operation == "+":
        print(usr_input[0] + usr_input[1])
        break
    elif usr_operation == "-":
        print(usr_input[0] - usr_input[1])
        break
    elif usr_operation == "*":
        print(usr_input[0] * usr_input[1])
        break
    elif usr_operation == "/":
        print(usr_input[0] / usr_input[1])
        break
    elif usr_operation == "s":
        print(usr_input[0] ** usr_input[1])
        break