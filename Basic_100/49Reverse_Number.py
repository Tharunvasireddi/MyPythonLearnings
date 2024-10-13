def Reverse(num):
    if num>=0 and num<=9 :
        return num
    else:
        sum=0
        while num>0:
            digit=num%10
            sum=10*sum+digit
            num//=10
        return sum
num=int(input("enter the number : "))
rev=Reverse(num)
print("reversed number of {0} is : ".format(num),rev) 