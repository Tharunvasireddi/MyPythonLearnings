def Power_set(my_set1):
    my_list=list(my_set1)
    result=[[]]
    for j in my_list:
           result += [i +[j] for i in result]
    return result
my_set1={1,2,3}
powerset=Power_set(my_set1)
print("Power set of {0} is :".format(my_set1),powerset)