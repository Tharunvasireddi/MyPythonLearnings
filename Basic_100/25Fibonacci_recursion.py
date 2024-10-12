def Fibonacci(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else :
        return Fibonacci(n-1)+Fibonacci(n-2)
    
num=int(input("enter the number : "))
print("the fibonacci series of number is :",end=" ")
for i in range(0,num):
    print(Fibonacci(i),end=" ")
