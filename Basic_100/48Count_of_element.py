def Count_of(my_list,num):
    count=0
    for i in my_list:
        if i == num:
            count+=1
    return count
list1=[1,2,2,3,2,4,5,62,5,2,1,3,7,8,10]
cont=Count_of(list1,1)
print("the count of Occurances of the element in the list is :",cont)