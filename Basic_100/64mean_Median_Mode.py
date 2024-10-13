def Mean(my_list):
    sum=0
    for i in my_list:
        sum+=i
    return sum/len(my_list)
def Meadian(my_list):
    if len(my_list)%2==0:
        return my_list[len(my_list)//2]
    else :
        ele1=my_list[len(my_list)//2]
        ele2=my_list[len(my_list)//2-1]
        elem=(ele1+ele2)//2
        return my_list[elem]
def maximum_count(my_list):
    count_list=[0]*len(my_list)
    for i in my_list:
        count_list[i]+=1
    max=count_list[0]
    idex=0
    for i in range(len(count_list)):
        if max<=count_list[i]:
            max=count_list[i]
            idex=i
    return idex
def Mode(my_list):
    return maximum_count(my_list)
my_list=[1,2,3,4,5,2,2,1,3,5,6,7]
print("mean of elements of {0} is :".format(my_list),Mean(my_list))
print("mediam of elements of {0} is :".format(my_list),Meadian(my_list))
print("mode of elements of {0} is :".format(my_list),Mode(my_list))