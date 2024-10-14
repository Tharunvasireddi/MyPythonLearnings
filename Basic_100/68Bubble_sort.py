def bubbleSort(my_list):
    for i in range(len(my_list)-1):
        for j in range(i+1,len(my_list)):
            if my_list[i]>my_list[j]:
                temp=my_list[i]
                my_list[i]=my_list[j]
                my_list[j]=temp
    return my_list
my_list=[1,2,5,6,2,3,9,10]
print("sorted array is : ",bubbleSort(my_list))