def linearSearch(my_list,tar):
    for i in my_list:
        if tar==i:
            return True
    return False
my_list=[1,5,24,7,56,100]
if linearSearch(my_list,24):
    print("element is present ")
else :
    print("element is absent ")