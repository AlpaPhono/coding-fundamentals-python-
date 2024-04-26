
# For loop solution
'''for i in range(5):
   name = str(input("Enter name"))
   print(f"{name} is great!\n") 
'''

'''
names = [input("what is your name?") for name in range(5)]
for name in names:
    print(f"{name} is great")
'''
    
# List comprehension
[print(f"{name} is great") for name in [input("enter a name") for x in range(5)]]