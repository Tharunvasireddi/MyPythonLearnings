num1=int(input("enter the number : "))
num2=int(input("enter the number : "))
min_num=min(num1,num2)
for i in range(2,min_num+1):
    if num1%i==0 and num2%i==0 :
        HCF=i
print("HCF of {0} and {1} is :".format(num1,num2),HCF)