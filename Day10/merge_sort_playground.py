from merge_sort_algorithm import *

from sorting_utilities import *


array_size = 20
lower = 100
upper = 200
array = generate_array_between(array_size, lower,upper)
print(f"Generatd an array of size {array_size} between {lower} and {upper}",array)

sorted_array = merge_sort(array=array)
print("sorted: ", sorted_array)