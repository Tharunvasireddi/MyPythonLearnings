def Intersection(my_list1,my_list2):
    my_set1=set(my_list1)
    my_set2=set(my_list2)
    my_set3=my_set1.intersection(my_set2)
    my_list3=list(my_set3)
    return my_list3
my_list1=[1,2,3,4,5]
my_list2=[2,3,10,5,6]
my_list3=Intersection(my_list1,my_list2)
print("intersection of {0} and {1} is : ".format(my_list1,my_list2),my_list3)