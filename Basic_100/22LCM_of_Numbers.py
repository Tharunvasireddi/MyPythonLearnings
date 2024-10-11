num1=int(input("enter the number : "))
num2=int(input("enter the number : "))
min_num=min(num1,num2)
hcf=1
for i in range(2,min_num+1):
    if num1%i==0 and num2%i==0 :
        hcf=i
lcm=(num1*num2)/hcf
print("LCM of {0} and {1} is :".format(num1,num2),lcm)