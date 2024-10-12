def Sum(n):
    if n==0:
        return 0
    else :
        return n+Sum(n-1)
    
num=int(input("enter the number "))
sum=Sum(num)
print("sum of natural numbers is : ",sum)
