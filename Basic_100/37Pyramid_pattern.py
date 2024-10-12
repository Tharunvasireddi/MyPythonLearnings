num=int(input("enter the value of rows : "))
for i in range(num):
    for j in range(2*num-1):
         if j>=num-1-i and j<=num-1+i :
            print("*",end=" ")
         else :
            print(" ",end=" ")
    print()