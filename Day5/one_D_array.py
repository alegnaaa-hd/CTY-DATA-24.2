one_d = list() # []
one_d.append(1)
one_d.append("hello")

one_d.append(3.5)
one_d.append(5.0)

one_d.append('c')

another_one_d = []
another_one_d.append("hi")
another_one_d.append("1")
another_one_d.append(6.58)
two_d = []
print("One dimensional array: ",one_d)

two_d.append(one_d)
two_d.append(another_one_d)

print("Two dimensional array: ",two_d)

a1d = ["hi", 25.3, ('hello',0,'1')]
b1d = [1.234, 56, None, True, False]

my_fun_2d_array = [a1d, b1d]
print("[")
for weird_1d_array in my_fun_2d_array:
    print("   ",weird_1d_array)

print("]")