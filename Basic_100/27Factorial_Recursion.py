def Factorial(n):
    if n==1 or n==1 :
        return 1
    else :
        return n*Factorial(n-1)
    
num=int(input("enter the number : "))
print("Factorial of {0} is : ".format(num),Factorial(num))