import random

def is_less_than(a:int,b: int) -> bool:
    return a < b
def swap(array: list[int], i:int, j:int):
    if i >= 0 and i < len(array) and j>=0 and j < len(array):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp


# generates an array of random number of size

def generate_array_between(size_array:int, lower:int, upper:int) -> list[int]:

    if size_array <= 0:
        return []
    array = [0]*size_array
    for i in range(size_array):
        array[i] = random.randrange(lower,upper)

    return array


def insertion_sort(array: list[int]) ->  list[int]: 
   # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


    
def selection_sort(array: list[int]) ->  list[int]: 


    n = len(array)
    for i in range(n):
        index_with_smallest = i
        for j in range(i+1, n):
            if is_less_than(array[j], array[index_with_smallest]):
                index_with_smallest = j
        swap(array, i, index_with_smallest)

