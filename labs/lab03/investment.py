'''
 Calculates how many years it will take an inital investment of £100 to grow to a target value of £1000
 if the interest rate is 10%
 TIP: Do not start writing code untill you've a plan of action
 '''
def invest(investment):
    years = 10
    rate = 1.10
    while years != 0:
        investment *= rate
        years -= 1
    return investment

def is_float(usr_input):
    while True:
        try:
            float(usr_input)
            break
        
        except TypeError:
            print("TypeError: Please input a number not a string.")
    return usr_input

def yearsCalc(invest, target_value, interest_rate):
    ''' Calculate how many years it would take to take an initial investment  to desired outcome:
        Args:
            invest (float): inital investment 
            target_value (float): outcome 
        Returns: 
            y (int): years it would take

        Raises:
            TypeError: If  user inputs wrong type on prompt

    '''
    y = 0
    rate = (interest_rate + 100)/100
    while invest <= target_value:
        invest *= rate
        y += 1

    return y





print(f"amount of years:\t {yearsCalc(100, 1000, 10)}")