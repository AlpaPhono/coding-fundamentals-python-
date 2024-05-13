import pytest, unittest
from finaltask.password_checker import Password_checker as pc

class TestPC:
        

    def setup_method(self,method):
        print("Setting up {}.".format(method))
        self.password = pc("Spr!ngW@ter") # Creates Password object to be tested against

    def teardown_method(self,method):   # Destroys password object after its tested against a method
        del self.password

    def test_length_rating(self):
        assert self.pc == 5


