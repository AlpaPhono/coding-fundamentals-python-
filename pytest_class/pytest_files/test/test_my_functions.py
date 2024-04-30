# Py test is widely used
# Plain assert statements
# flexible
# automatic test detection (test_ dor files test_ for funtions, Test_ for class)
# fixtures = set certain conditions, parametisations - pass through different sets of date to one test

import pytest
from pytest_files.my_functions import *

def test_answer():
    assert add(1,2) == 3
    assert add(1, 2) == 1 + 2
    result = add(1,2)
    assert result == 3
    assert add(-1.-1) == -2
    assert add(0,0) == 0

def test_divide(a, b):
    with pytest.raises(ZeroDivisionError):
      divide(10,0)
#--------------
# Make a function with test_
#--------------
    

class Test_area:
    
    def setup_method(self):
        return self.x = Area(5,10)

    def test_area(self):
        assert self.x.area_calc() == 50

    
    def teardown_method(self):
        del self.x

    
    
# fixture 
@pytest.fixture
def x():
    return Area(10,5)

def test_x(x):
    assert x.area_calc() == 50

    # Parameterisation

@pytest.mark.parametrize("width,length,area",[(5,10,500), 10,10,100])