def quick_sort(arr,low,high):
    if low>=high:
        return
    pivot=arr[low]
    right=high
    left=low
    while left<=right:
        while arr[left]<pivot:
            left+=1
        while arr[right]>pivot:
            right-=1
        if left<=right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    quick_sort(arr,low,right)
    quick_sort(arr,left,high)
my_list=[1,-1,0,5,3,2,7]
quick_sort(my_list,0,len(my_list)-1)
print(my_list)