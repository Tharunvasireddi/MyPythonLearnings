def Cube(num):
    pow=1
    for i in range(3):
        pow=pow*num
    return pow
num=int(input("enter the number of natural numbers : "))
cube_list=[]
sum=0
for i in range(1,num+1):
    sum+=Cube(i)
print("the sum of cubes is :",sum)