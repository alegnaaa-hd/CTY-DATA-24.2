
from binary_search import binary_search_recursive
"""
Suppose we are performing a binary search on a sorted array called numbers initialized as follows:
// index           0   1   2   3   4   5   6   7   8   9  10  11  12  13
"""
numbers = [-30, -9, -6, -4, -2, -1,  0,  2,  4, 10, 12, 17, 22, 30]

# search for the value -5

index = binary_search_recursive(numbers, -5, 0, len(numbers)-1)
print(index)

"""


Write the indexes of the elements that would be examined by the binary search (the mid values in our algorithm's code) and write the value that would be returned from the search. Assume that we are using the binary search algorithm shown in chapter 13 of the Building Java Programs 5th Edition textbook.


"""