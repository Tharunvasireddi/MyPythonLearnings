def binarySearch(arr, element):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            high = mid - 1
        else:
            low = mid + 1
    return -1

