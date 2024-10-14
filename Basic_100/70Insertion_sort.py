def insertion_sort(my_list):
    for i in range(len(my_list)-1):
        j=i+1
        while j>0:
            if my_list[j]<=my_list[j-1]:
                temp=my_list[j]
                my_list[j]=my_list[j-1]
                my_list[j-1]=temp
            else :
                break
            j-=1
    return my_list
my_list=[-1,1,-19,20,5,7]
print("the sorted array is :",insertion_sort(my_list))