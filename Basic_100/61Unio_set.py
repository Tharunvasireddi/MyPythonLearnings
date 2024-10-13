def Union(my_set1,my_set2):
    my_set3=set()
    my_set3=my_set1.union(my_set2)
    return my_set3
my_set1={1,2,3,4,5}
my_set2={6,7,8,9,10}
my_set3=Union(my_set1,my_set2)
print("Union of {0} and {1} is :".format(my_set1,my_set2),my_set3)