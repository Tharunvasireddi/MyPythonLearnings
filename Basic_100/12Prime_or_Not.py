num=int(input("enter the number : "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("given number is prime number ")
else :
    print("given number is not prime number")