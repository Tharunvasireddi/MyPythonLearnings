num=int(input("enter the number : "))
if num == 0 or num == 1:
    print("Factorial of given number is :",1)
else :
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of given number is : ",fact)
