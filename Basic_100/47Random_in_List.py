def Random(my_list):
    import random
    ran= random .randint(0,len(my_list)-1)
    return my_list[ran]
list1=[i for i in range(0,100,5)]
random_=Random(list1)
print("the random element of list is : ",random_)