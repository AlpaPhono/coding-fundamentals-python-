# Ask user to input a an integer.
prompt = "input an integer"

'''
def factorial(n):
    iteration = 1
    total = 0
    while iteration < n + 1:
        step = 1
        step_above = step + 1
        multi = step * step_above
        total += multi

        
I was over doing it.. the solution is much simpler.        
        '''   

def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    print(f"fact:\t{fact}")

while True:
    try:
        usr_num = int(input(prompt))
        break
    except ValueError():
        print("Please input a number: ")

factorial(usr_num)

