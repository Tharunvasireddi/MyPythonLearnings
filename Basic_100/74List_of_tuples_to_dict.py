def conversion(my_list):
    dict={}
    for i in range(len(my_list)):
        dict[i]=my_list[i]
    return dict
my_list=[(1,2,3),("tharun","vasu","ananth"),(19,18,23)]
dict=conversion(my_list)
print("the dictionaary with tuple is :",dict)
