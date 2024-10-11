num=int(input("enter the number : "))
temp,dup,sum=num,num,0
count=0
while temp>0:
    count+=1
    temp//=10
while dup>0:
    digit = dup%10
    sum+=digit**count
    dup//=10
if num==sum:
    print("given number is Armstrong Number")
else :
    print("given number is not Armstrong Number")
