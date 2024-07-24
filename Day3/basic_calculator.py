from functions import *
(number1, number2) = get_two_numbers_from_user()

#print("Enter + to add")
operation = str(input("Enter + to add\nEnter - to subtract\nEnter * to multiply\nEnter / to divide\n : "))
a = "+"
s = "-"
m ="*"
d="/"

x = float(number1)
y = float(number2)
if operation == a:
    result = add(x,y)
elif operation == s:
    result = subtract(x,y)
elif operation == m:
    result = multiply(x,y)
elif operation == d:
    result = divide(x,y)

print(number1," ", operation, " " ,number2," = ", result )