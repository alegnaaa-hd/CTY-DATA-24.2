import math

class Calculator:

    def __init__(self):
        self.number1 = 0.0
        self.number2 = 0.0

    def add(self):
        return self.number1 + self.number2

    def subtract(self): 
        return self.number1 - self.number2

    def multiply(self): 
        return self.number1 * self.number2
    def divide(self): 
        if self.number1 != 0.0:
            return self.number1 / self.number2
    def get_two_numbers_from_user(self):
        # get number1, and number2 from user
        
        self.number1 = float(input("Enter number1: "))
        self.number2 = float(input("Enter number2: "))
        #return (self.number1,self.number2)
    def exponent(self):
        return self.number1 ** self.number2

    def sine(self):
        return math.sin(self.number1)
    def cosine(self):
        return math.cos(self.number1)

    def tangent(self):
        return math.tan(self.number1)

        

"""
basic_calculator = Calculator()

scientific_calculator = Calculator()

basic_calculator.get_two_numbers_from_user()

scientific_calculator.number1 = basic_calculator.number1
scientific_calculator.number2 = basic_calculator.number2
# exp = basic_calc.number1 ** basic_calc.number2
exp = scientific_calculator.exponent()
# basic_calc.number1 + basic_calc.number2 
print("exp: ",exp)

"""
