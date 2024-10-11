num=int(input("enter the number : "))
n1,n2,n3=0,1,0
print("the fibonacci series is :",n1,n2,end=" ")
for  i in range(num):
   n3 = n1+n2
   print(n3,end=" ")
   n1=n2
   n2=n3
