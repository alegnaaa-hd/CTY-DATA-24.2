import math
def add(number1, number2): 
    return number1 + number2

def subtract(number1, number2): 
    return number1 - number2
def multiply(number1, number2): 
    return number1 * number2
def divide(number1, number2): 
    if number2 != 0.0:
        return number1 / number2
def get_two_numbers_from_user():
    # get number1, and number2 from user
    number1 = 0.0
    number2 = 0.0
    number1 = float(input("Enter number1: "))
    number2 = float(input("Enter number 2: "))
    return (number1,number2)
def exponent(base, power):
    return base ** power

def sine(number):
    return math.sin(number)
def cosine(number):
    return math.cos(number)

def tangent(number):
    return math.tan(number)
    
