#Create an IF statement to see if the person is equal 18 or over. 


age = 19
if age >= 18:
    print("You are in catagory A:")
if 18 > age >= 16:
    print("You are in catagory B:")
if age < 16:
    print("You are in caragory C")

print("\n, using ELIF:\n")
#----------------------
# Using elif
#----------------------

age2 = 12
if age2 >=18 :
    print("You are in catagory A:")
elif age2 >= 16:
    print("You are in catagory B:")
else:
     print("You are in catagory C")