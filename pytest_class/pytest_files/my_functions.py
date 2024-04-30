def add(a,b):
    return a + b

def divide(a,b):
    return a / b

class Area:
    def __init__(self,length,width) -> None:
        self.length = length
        self.width = width

    def area_calc(self):
        return self.length * self.width