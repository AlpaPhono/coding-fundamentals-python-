# Weight converter app  0.45
#++++++++++++++++++++++++++
# user input 
#++++++++++++++++++++++++++
conversion = 2.2046

while True:
    unit = str(input("kg or lbs"))
    unit.lower()
    if unit == "kg" or unit == "lbs":
        break
    else:
        print("wrong input, try again!")


weight = int(input("how much is the weight"))

#+++++++++++++++++++++++++
# Conversion
#+++++++++++++++++++++++++
if unit == "kg":
    newWeight = weight * conversion
    print(newWeight)
else:
    newWeight = weight / conversion
    print(newWeight)
