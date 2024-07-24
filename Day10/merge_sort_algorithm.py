from sorting_utilities import *


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        # here we have an array whose size is greater than 1, 
        # and it is not sorted
        n = len(array)
        mid = n // 2
        # split the array into left and right
        left_array = array[:mid]
        right_array = array[mid:]
        # recusrively call merge_sort on both left and right
        sort_left_array = merge_sort(left_array)
        sorted_right_array = merge_sort(right_array)
        # combine the sorted left an sorted right into a nicely sorted
        final_sorted_array = merge(sort_left_array,sorted_right_array)
        return final_sorted_array
    

# renamed combine_sorted to merge
def merge(array1, array2):
    array3_size = len(array1) + len(array2)
    array3 = [0] * array3_size # new int[array1.length + array2.lengt]
    index1 = 0
    index2 = 0 
    index3 = 0
    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] <= array2[index2]:
            array3[index3] = array1[index1]
            index1 += 1
        else:
            array3[index3] = array2[index2]
            index2 += 1
        index3 += 1

    if index1 < len(array1):
        # left over from array1
        # while loop 1  to copy left over from array1 :
        while index1 < len(array1):
            array3[index3] = array1[index1]
            index1 += 1
            index3 += 1
    elif index2 < len(array2):
        # left over from array2         

        # while loop 2  to copy left over from array2 :
        while index2 < len(array2):
            array3[index3] = array2[index2]
            index2 += 1
            index3 += 1

    return array3

