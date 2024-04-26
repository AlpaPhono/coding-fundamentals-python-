#2. While loop that satrts at one and ends at 100
'''
def one_to_100():
    count = 1
    while count < 101:
        print(count)
        count +=1

one_to_100()
'''

#3. That calculates and displays each number and its square
'''
def one_to_100_square():
    count = 1
    while count < 101:
        print(f'''
#{count} and its square is {count**2}
''')
        count +=1

one_to_100_square()
'''


#4. End the loop if that square is bigger than 2000.  
def one_to_100_square():
    count = 1
    while count < 101:
        if count**2 > 2000:
            print(f'''
    {count} and its square is {count**2}
    ''')
            count +=1
        else: break

one_to_100_square()