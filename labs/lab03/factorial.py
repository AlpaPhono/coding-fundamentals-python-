# Ask user to input a an integer.
prompt = "input an integer"


def factorial(n):
    iteration = 1
    while iteration < n + 1:
        shrine = []
        tot = iteration * (iteration - 1)
        shrine.append(tot)
        iteration += 1
    


while True:
    try:
        usr_num = int(input(prompt))
        break
    except ValueError():
        print("Please input a number: ")

print(factorial(usr_num))

