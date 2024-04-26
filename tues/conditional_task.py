# user input for grade/mark
# if mark is greater than 85 print distinction
# if mark is between 65 and 85 print pass 
# anything else print fail
# use if -if else or if elif - else


grade = int(input("What was your grade?: \n"))
passs = 85
fail = 65

if grade > passs:
    print("Distinction")
elif grade > fail and grade < passs:
    print("pass")
else:
    print("fail")

# example
if 0 < deport <=100 or password == "password1":
    print()
else:
    print("failed")