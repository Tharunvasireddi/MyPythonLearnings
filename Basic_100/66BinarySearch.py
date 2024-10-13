def binarySearch(arr, element):
    low, high = 0, len(arr)-1
    while low <high:
        mid=(low+high)//2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1
my_list=[1,2,3,4,5]
print(binarySearch(my_list,4))
