def binarySearch(arr, element):
    low, high = 0, len(arr)-1
    while low <high:
        mid=(low+high)//2
        if arr[mid] == element:
            return True
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return False
my_list=[1,2,3,4,5]
if binarySearch(my_list,3):
    print("targeted element is present ")
else :
    print("targeted element is absent")

