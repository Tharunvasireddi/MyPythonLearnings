def Cube(num):
    pow=1
    for i in range(3):
        pow=pow*num
    return pow
num=int(input("enter the number :"))
cube=Cube(num)
print("the cube of the {0}  is : ".format(num),cube)
