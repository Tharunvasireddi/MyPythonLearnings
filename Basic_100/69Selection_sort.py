def swap(my_list,high,i):
    temp=my_list[i]
    my_list[i]=my_list[high]
    my_list[high]=temp
def maximum(my_list,last):
    max=my_list[0]
    ind=0
    for i in range(last):
        if max<my_list[i]:
            max=my_list[i]
            ind=i
    return ind
def selectionSort(my_list):
    for i in range(len(my_list)):
        high=len(my_list)-i-1
        ind=maximum(my_list,high+1)
        swap(my_list,high,ind)
    return my_list

my_list=[1,2,1,-1,6,3,0]
print("the sorted array is :",selectionSort(my_list))
      
