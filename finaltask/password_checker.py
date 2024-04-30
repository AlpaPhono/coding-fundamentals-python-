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
    def __init__(self,password):

        self.password = password

    def pattern_search(self):
        password = self.password

        strongest_pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d+)(?!=.*\s).*"
        strongest_match = re.search(strongest_pattern,password)

        average_pattern =r"(?=.*[a-z])(?=.*\d+)(?!=.*\s)(?!=.*[A-Z]).*"
        average_match = re.search(average_pattern,password)

        weak_pattern = r"(?=.*[a-z])(?!=.*\s)(?!=.*\d+)v(?!=.*[A-Z]).*"
        weak_match = re.search(weak_pattern,password)

        weakest_pattern = r"(?=.*[a-z])(?!=.*\d+)(?!=.*[A-Z])(?!=.*\s).*"   # this pattern would have been simpler: r"^[a-z]+$"
        weakest_match = re.search(weakest_pattern,password)

        if strongest_match:
            print("This is a strong password")
        elif average_match:
            print("This is an average password")
        elif weak_match:
            print("This is a weak password")
        elif weakest_match:
            print("This password is too weak.")


