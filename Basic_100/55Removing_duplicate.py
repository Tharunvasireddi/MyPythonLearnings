def Remove_dup(my_list):
    new_list=[]
    my_set=set()
    for i in my_list:
        if i not in my_set:
                new_list.append(i)
                my_set.add(i)
    return new_list
my_list=[1,2,3,5,2,6,5,4,1]
my_list1=Remove_dup(my_list)
print("After removing duplicates in {0} is :".format(my_list),my_list1)