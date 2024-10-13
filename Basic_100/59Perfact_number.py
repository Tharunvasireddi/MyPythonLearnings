def Perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    else:
        return False
num=abs(int(input("enter the number : ")))
if Perfect(num):
    print("{0} is perfect number".format(num))
else :
    print("{0} is not perfect number".format(num))