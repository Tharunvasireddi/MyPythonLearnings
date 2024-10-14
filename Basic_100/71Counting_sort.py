def countSort(my_list):
    max=my_list[0]
    for i in my_list:
        if max<i:
            max=i
    max=max+1
    count=[0]*max
    for i in my_list:
        count[i]=count[i]+1
    ind=0
    for i in range(len(count)):
        while count[i]>0:
            my_list[ind]=i
            ind+=1
            count[i]-=1
    return my_list
my_list=[1,0,3,5,6,7,13]
print("sorted array is :",countSort(my_list))