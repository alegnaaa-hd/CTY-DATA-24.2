def binary_search_iterative(arr, target):
    start, stop = 0, (len(arr) - 1)

    while start <= stop:
        mid = (start + stop) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            stop = mid - 1

    return -1  # Target not found


def binary_search_recursive(arr, target, start, stop):
    if start > stop:
        return -1  # Target not found

    mid = (start + stop) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, stop)
    else:
        return binary_search_recursive(arr, target, start, mid - 1)
