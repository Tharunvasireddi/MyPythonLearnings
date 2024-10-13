def Minimum(my_list):
    min=my_list[0]
    for i in range(len(my_list)):
        if min>my_list[i]:
            min=my_list[i]
    return min
my_list=[1,2,3,4,50,6,-1]
min=Minimum(my_list)
print("minimum element of {0} is :".format(my_list),min)
