def Sum_of(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num//=10
    return sum
num=abs(int(input("enter the number :")))
sum=Sum_of(num)
print("Sum of digits in the {0} is :".format(num),sum)