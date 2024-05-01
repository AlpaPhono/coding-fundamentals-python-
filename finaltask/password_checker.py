'''
Application that checks the strength of a password
Requirements:
    - Write a class that has a method that checks password strength.
    - Use factors like length, upper/lower case and if it has a number and special characters
    - Ratings should be very weak - weak - moderate - strong - very strong
    - Check against a list of common paswords 10-20 common passwords = very weak
    - User input that loops untill the user quits
    - A dictionary that returns a history of passwords /strengths whilst in the loop

    Code must be pushed to a rep

    2nd stretch goal
        write tests and achieve a high score in pylint
'''

import re




class Password_checker():

    very_weak_passwords = ['123456','123456789','qwerty','password','qwerty123','password1','1q2w3e','hello','passw0rd','PassWord']

    def __init__(self,password):
        self.password = password   
    
    def length_rating(self):
        pass_length = len(self.password)
        length_rating = 0
        if 0 < pass_length < 5:
            length_rating = 1
        elif 4 < pass_length < 8:
            length_rating = 2
        elif 7 < pass_length < 10:
            length_rating = 3
        elif 9 < pass_length: 
            length_rating = 5
        return length_rating

        

        


    def pattern_search(self):
        password = self.password
        pattern_rating = 0

        strongest_pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d+)(?!=.*\s).*"
        strongest_match = re.search(strongest_pattern,password)

        average_pattern =r"(?=.*[a-z])(?=.*\d+)(?!=.*\s)(?!=.*[A-Z]).*"
        average_match = re.search(average_pattern,password)

        weak_pattern = r"(?=.*[a-z])(?!=.*\s)(?!=.*\d+)v(?!=.*[A-Z]).*"
        weak_match = re.search(weak_pattern,password)

        weakest_pattern = r"(?=.*[a-z])(?!=.*\d+)(?!=.*[A-Z])(?!=.*\s).*"   # this pattern would have been simpler: r"^[a-z]+$"
        weakest_match = re.search(weakest_pattern,password)

        if strongest_match:
            pattern_rating = 4
            #print("This is a strong password")
        elif average_match:
            pattern_rating = 3
            #print("This is an average password")
        elif weak_match:
            #print("This is a weak password")
            pattern_rating = 2
        elif weakest_match:
            pattern_rating = 1
            #print("This password is too weak.")
        
        return  pattern_rating

    def how_many_special_characters(self):
        password = self.password
        spec_char = 0
        char_rating = 0
        for char in password:
            if not char.isalnum() and not char.isspace():
                spec_char += 1
        
        if spec_char == 0:
            char_rating = 1
        elif spec_char < 3:
            char_rating = 2
        elif spec_char < 4:
            char_rating = 3
        elif spec_char > 5:
            char_rating = 4

        return char_rating 
    
    def pass_rank(self, len_rate, pattern_rate, char_rate):
    
        final_rating = len_rate + pattern_rate + char_rate

        if 0 < final_rating < 5:
            print("weak")
        elif 4 < final_rating < 8:
            print("Medium")
        elif 7 < final_rating < 12:
            print("Strong")
        elif 11 < final_rating < 16:
            print("Very Strong")
    