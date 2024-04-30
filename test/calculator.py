# Unit test 
# More complicated than pytest
# Part of standard libray
# test cases by subclassing uniitest. testCase 
# Can have multiple test methods(assertions) per test case
# buit on j-unit

class Calculator:
    
    def add(self, a, b):
        if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
            raise TypeError("Custom Error: Inputs must be numeric")




        return a + b

