from binary_search import binary_search_iterative,binary_search_recursive


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# Iterative
result_iterative = binary_search_iterative(arr, target)
print(f'\nIterative: Element found at index {result_iterative}' if result_iterative != -1 else 'Element not found')

# Recursive
result_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f'\nRecursive: Element found at index {result_recursive}' if result_recursive != -1 else 'Element not found')
