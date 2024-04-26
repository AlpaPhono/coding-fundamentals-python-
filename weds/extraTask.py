#Sam has been dumped by his girlfriend so he's gone into the local milk 
#bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
#milkshakes, 
#differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
#number corresponding 
#to the relevant flavour - this list is displayed every iteration. 
#If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
#If he orders but can't pay he's thrown out.
import sys
#======================
# VARIABLES 
#======================

budget = 5.00 #float(input())
expenditure = 0
menu = '''
Todays menu:\n
1. Vanilla\t\t     £3.00\n
2. Strawberry\t\t  £2.50\n
3. Mango\t\t       £5.00\n
\n
Please select the number corrosponding to the shake you want.\n\n

Enter Q to leave.\n 
'''
shakes = {1: 3.00, 2:2.50,3:5.00}   # numbers corrospond with numbers in the menu
prompt = "What can I fix you?:"


while True:
    #------------
    # Menu + Greeting
    #------------
    print(prompt)
    print(menu,"\n")
    budget = budget - expenditure
    #
    #-----------
    if budget >= shakes[2]:
        #
        #------------
        
        #------------------------
        # User shake selection
        #------------------------
        while True:
            usr_option = input()
            if int(usr_option) in range(1,4):
                # Expenditure
                if budget > shakes[int(usr_option)]:
                    expenditure = budget - shakes[int(usr_option)]
                    print("Thanks for your purchase!:")
                    break
                else:
                    print("you do not have enough money: \n")
                    sys.exit()
            elif usr_option.upper() == "Q":
                print("Thanks for your patronage!: ")
                break
            else:
                print("wrong option. Please select either 1,2 or 3 or LEAVE!:\n")
        #
        #--------------------------
        #--------------------------
    else:
        print("BROKE ASS DUMB ASS GET OUT!")
        break            


  #  if usr_response in shakes.keys.upper():
#   usr_response = str(input()).upper()
        


    