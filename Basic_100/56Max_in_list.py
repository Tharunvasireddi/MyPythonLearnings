def Maximum(my_list):
    max=my_list[0]
    for i in range(1,len(my_list)):
        if max <= my_list[i]:
            max=my_list[i]
    return max
my_list=[1,10,11,13,4,56,100]
max=Maximum(my_list)
print("Maximum element in the {0} is : ".format(my_list),max)