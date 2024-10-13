def Second_Max(my_list):
    max1=my_list[0]
    max2=my_list[0]
    for i in range(len(my_list)):
        if max1<=my_list[i]:
            max2=max1
            max1=my_list[i]
    return max2
my_list=[1,10,11,13,4,56,57,100,1000]
max2=Second_Max(my_list)
print("Second maximum element of {0} is :".format(my_list),max2)